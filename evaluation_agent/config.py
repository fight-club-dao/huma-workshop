import os

ea = os.environ.get('EA', "0xA057173A66f90a15D0295e5502752140362539D3")
ea_key = os.environ.get('EA_KEY', "0x5de4111afa1a4b94908f83103eb1f1706367c2e68ca870fc3fb9a804cdab365a")
borrower_whitelist_contract = os.environ.get('BORROWER_WHITE_LIST_CONTRACT_ADDR', "0x0B2813424E99f4Bd58d0545509EAfBb8039F570d")
signals_endpoint = os.environ.get('SIGNALS_ENDPOINT', "http://127.0.0.1:8001/fetch")  # "https://dev.goerli.signals.huma.finance/fetch"
provider_url = os.environ.get('PROVIDER_URL', 'https://eth-goerli.g.alchemy.com/v2/ugw2EcIzTw9sG99pp46rSa0NBZTHcwip')  # , "http://127.0.0.1:8001/fetch")  # "https://dev.goerli.signals.huma.finance/fetch"

print('signals_endpoint', signals_endpoint)
print('borrower_whitelist_contract', borrower_whitelist_contract)
print('ea', ea)
