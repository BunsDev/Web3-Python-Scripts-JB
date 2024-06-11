from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/YOUR_API_KEY_HERE'
web3 = Web3(Web3.HTTPProvider(infura_url))

wallet_address = '0x123e710c69b6806ef32Cf52e49dCC5EEEc368a22'
token_contract_address = '0x7eae7422f633429EE72BA991Ac293197B80D5976'

token_abi = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    }
]

token_contract = web3.eth.contract(address=token_contract_address, abi=token_abi)
balance = token_contract.functions.balanceOf(wallet_address).call()
decimals = token_contract.functions.decimals().call()
adjusted_balance = balance / (10 ** decimals)
print(f"Token Balance: {adjusted_balance}")
