import argparse
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/YOUR_API_KEY_HERE"
web3 = Web3(Web3.HTTPProvider(infura_url))

parser = argparse.ArgumentParser(description="Look up an Ethereum Name Service (ENS) name.")
parser.add_argument("name", type=str, help="The ENS name to look up, e.g., james.eth")
args = parser.parse_args()

address = web3.ens.address(args.name)

if address:
    print(f"Address found for {args.name} - {address}")
else:
    print(f"ENS name {args.name} could not be found")
