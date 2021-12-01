# import
import json
# use official coinbase api
### https://pypi.org/project/coinbase/
### https://github.com/coinbase/coinbase-python/
from coinbase.wallet.client import Client

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)

# Init coinbase connection
def get_client(json_config:json):
    coinbase_api_key = ""
    coinbase_api_secret = ""
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];
    if (coinbase_api_key != "" and coinbase_api_secret != "") :
        return Client(coinbase_api_key, coinbase_api_secret)

# Append all pagined accounts to only one array
def get_all_accounts(client: object()):
    all_accounts = []
    starting_after = None
    # infinite loop
    while True:
        accounts = client.get_accounts(limit=100, starting_after=starting_after)
        # if pagination exist then push all account in array and loop again
        if accounts.pagination.next_starting_after is not None:
            starting_after = accounts.pagination.next_starting_after
            for account in accounts.data:
                all_accounts.append(account)
            time.sleep(1)
        # if pagination don't exist then push all account in array and exit loop
        else:
            for account in accounts.data:
                all_accounts.append(account)
            break
    return all_accounts

# Main Script
client = get_client(json_config)
accounts = get_all_accounts(client)
total = 0
for currency in accounts:
    amount = float(currency.native_balance.amount)
    if amount > 0:
        total += amount
        print("# " + currency.currency + " : " + str(amount) + " " + currency.native_balance.currency)
print("########## Total : " + str(total))
