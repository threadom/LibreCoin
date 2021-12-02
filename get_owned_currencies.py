# import JSON
import json
# import Regular Expression
import re 
# import Time (for sleep)
import time
# import Operator (for sorted)
import operator

# use official coinbase api
### https://pypi.org/project/coinbase/
### https://github.com/coinbase/coinbase-python/
from coinbase.wallet.client import Client

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

########################################################
# Init coinbase connection
def get_client(json_config:json):
    print("get_client")
    coinbase_api_key = ""
    coinbase_api_secret = ""
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];
    if (coinbase_api_key != "" and coinbase_api_secret != "") :
        return Client(coinbase_api_key, coinbase_api_secret)


########################################################
# Append all pagined accounts to only one array
g_all_accounts = {}
def get_all_accounts(client: object):
    print("get_all_accounts")

    # read from globals if exist
    global g_all_accounts
    if len(g_all_accounts) > 0:
        return g_all_accounts

    # do it if nothing else exist
    all_accounts = {}
    starting_after = None
    # infinite loop
    while True:
        accounts = client.get_accounts(limit=25, starting_after=starting_after)
        # if pagination exist then push all account in array and loop again
        if accounts.pagination.next_starting_after is not None:
            starting_after = accounts.pagination.next_starting_after
            for account in accounts.data:
                all_accounts[account.currency] = account
            time.sleep(1)
        # if pagination don't exist then push all account in array and exit loop
        else:
            for account in accounts.data:
                all_accounts[account.currency] = account
            break

    # init globals before return
    g_all_accounts = all_accounts
    return g_all_accounts


########################################################
# sort transaction by transaction created date reversed
def sort_owned_currencies_by_value(owned_currencies: object):
    return dict(sorted(owned_currencies.items(), key=operator.itemgetter(1), reverse=True))


########################################################
# get own currencies
g_owned_currencies = {}
def get_owned_currencies(accounts: json):
    print("get_owned_currencies")
    global g_owned_currencies

    # read from globals if exist
    if len(g_owned_currencies) > 0:
        return g_owned_currencies 

    # do it if nothing else exist
    owned_currencies = {}
    for currency in accounts:
        balance = float(accounts[currency].native_balance.amount)
        if (balance > 0):
            owned_currencies[currency] = float(accounts[currency].native_balance.amount)

    # init globals before return
    g_owned_currencies = sort_owned_currencies_by_value(owned_currencies);
    return g_owned_currencies


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ MAIN SCRIPT ~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)

g_client = get_client(json_config)
g_all_accounts = get_all_accounts(g_client)
g_owned_currencies = get_owned_currencies(g_all_accounts)
print(currencies)