import json

from coinbase.wallet.client import Client

def lc_connect(json_config: json):
    print("lc_connect")
    coinbase_api_key = ""
    coinbase_api_secret = ""
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];
    if (coinbase_api_key != "" and coinbase_api_secret != "") :
        return Client(coinbase_api_key, coinbase_api_secret)
