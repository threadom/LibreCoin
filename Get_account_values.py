# import
import json
from coinbase.wallet.client import Client

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)

# Init coinbase connection
def coinbase_connect(json_config:json):
    coinbase_api_key
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];
    if (coinbase_api_key != "" and coinbase_api_secret != "") :
        return Client(coinbase_api_key, coinbase_api_secret)

client = coinbase_connect(json_config)


currencies_list = [
    "ETH",
    "BTC",
    "LINK",
    "MANA",
    "FIL",
    "MKR",
    "ADA",
    "SHIB",
    "XLM",
    "UNI",   
    "LTC",
    "ALGO",
    "AMP",
    "BAT",
    "DOGE",
    "OXT",
    "XTZ",
    "CRO",
    "ANKR",
    "SOL",
    "CTSI",
    "NU",
    "FET",
    "CLV",
    "AUCTION",
    "LRC",
    "GRT",
    "SKL",
    "ICP",
    "FORTH",
    "DAI",
    "ALCX",
    "GALA",
    "POLY"
    ]

def total():    
    total = 0

    for c in currencies_list:
        total += valeur(c)
    return round(total, 2)

def valeur(wallets: str):
    account = client.get_account(wallets)
    #convert to dict.
    accountdict = json.loads(json.dumps(account))

    #using dict to get the current BTC balance
    balance = round(float(accountdict['balance']['amount']),2)
    nativebalance = round(float(accountdict['native_balance']['amount']),2)
    print (wallets , "Quantité ",  balance, " Valeur ", nativebalance, "EUR" )
    return float(accountdict['native_balance']['amount'])



total()
print("Total: ", total(), "EUR")
