from typing import Any, Dict, List
import requests
import config

def fetch_signal(signal_names: List[str], adapter_inputs: Dict[str, Any]) -> Dict[str, Any]:
   """Fetch signals from the decentralized signal portfolio service.
   
   For more details about DSP service, see https://github.com/00labs/huma-signals/tree/main/huma_signals
   """
   request = {"signal_names": signal_names, "adapter_inputs": adapter_inputs}
   print(request)
   response = requests.post(config.signals_endpoint, json=request)
   print(response.text)
   if response.status_code != 200:
       raise ValueError(f"Error fetching signals: {response.text}")
   return {k: v for k, v in response.json().get("signals").items() if k in signal_names}


def aave_liquidity_interest_rate(usage_rate: float) -> float:
    optimal_usage_rate = 0.9
    if usage_rate <= optimal_usage_rate:
        return 0.005 + (usage_rate / optimal_usage_rate) * 0.04
    else:
        return 0.05 + ((usage_rate - optimal_usage_rate) / (1 - optimal_usage_rate)) * 0.1

def underwrite(huma_pool, **kwargs):
    """
    The interface function between an EA and Huma EA service
    :param huma_pool: the object that represents huma pool contract
    :param **kwargs
        poolAddress:        str: the address for the destiny huma pool
        borrowerWalletAddress:      str: the borrower's wallet address
    :return: returns corresponding fields to UI
    """

    borrower_wallet_address = kwargs["borrowerWalletAddress"]  # noqa

    # to be removed
    result = {
            "creditLimit": int(10000*10**6),
            "intervalInDays": 30,
            "remainingPeriods": 12,
            "aprInBps": 0
        }
    
    signal_names = [
        "allowlist_contract.on_allowlist",
        'ethereum_wallet.total_income_90days',
        'spectral_wallet.probability_of_liquidation',
        'lending_pool.total_assets',
        'lending_pool.total_supply',
    ]

    adapter_inputs = {
        "borrower_wallet_address": borrower_wallet_address,
        "contract_address": config.borrower_whitelist_contract,
        'pool_address': huma_pool.pool_address,
        'hdt_address': config.hdt_token_address,
        "chain": "GOERLI",
    }

    # TODO: add check here for recency of spectral wallet signal
    max_prob_of_liquidation = 95
    signals = fetch_signal(signal_names, adapter_inputs)
    prob_liquidation_rate = signals.get('spectral_wallet.probability_of_liquidation')
    print('is allowed to borrow', signals.get('allowlist_contract.on_allowlist'))
    print('probability_of_liquidation', signals.get('spectral_wallet.probability_of_liquidation'))
    if (
            signals.get('allowlist_contract.on_allowlist') and
            prob_liquidation_rate <= max_prob_of_liquidation
    ):
        # TODO: convert eth to usd taking a quick hack here assuming 1500 usd per eth
        assets = signals.get('ethereum_wallet.total_income_90days') * 1500  # check the price of ETH
        max_pct = 0.3
        min_borrow_amt = 5000
        max_borrow_amt = max([assets * 0.36, min_borrow_amt])  # want 36% for debt to asset ratio

        usage_rate = signals.get('lending_pool.total_assets') / signals.get('lending_pool.total_supply')
        print('usage_rate', usage_rate)
        rate = aave_liquidity_interest_rate(usage_rate) + 0.1 * (prob_liquidation_rate / 100)
        pct = min([rate, max_pct])
        print('pct', pct)
        result = {
            "creditLimit": int(max_borrow_amt*10**6),
            "intervalInDays": 30,
            "remainingPeriods": 12,
            "aprInBps": int(pct*100)
        }
    else:
        raise Exception("account not allowed")

    print(result)
    return result  # noqa
