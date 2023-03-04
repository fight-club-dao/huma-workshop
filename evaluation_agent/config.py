import os

ea = os.environ.get('EA', "0xb08a809428A69218B35647d79d90F90DdF295881")
ea_key = os.environ.get('EA_KEY')
borrower_whitelist_contract = os.environ.get('BORROWER_WHITE_LIST_CONTRACT_ADDR', "0x6842393062367bbBeAa61185836D18d50a50A0bf")
signals_endpoint = os.environ.get('SIGNALS_ENDPOINT', "http://127.0.0.1:8001/fetch")  # "https://dev.goerli.signals.huma.finance/fetch"
provider_url = os.environ.get('PROVIDER_URL', 'https://eth-goerli.g.alchemy.com/v2/ugw2EcIzTw9sG99pp46rSa0NBZTHcwip')  # , "http://127.0.0.1:8001/fetch")  # "https://dev.goerli.signals.huma.finance/fetch"

print('signals_endpoint', signals_endpoint)
print('borrower_whitelist_contract', borrower_whitelist_contract)
print('ea', ea)
