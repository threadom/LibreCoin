import json
from coinbase.wallet.client import Client
cb_api_key = ""
cb_api_secret = ""
client = Client(cb_api_key, cb_api_secret)

def get_accounts(client):
    accounts = client.get_accounts()
    return accounts

accounts = get_accounts(client)
jsonString = json.dumps(accounts)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
