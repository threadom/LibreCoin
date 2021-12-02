# import JSON
import json
# import for sort (and filters)
import re 
import operator
# import for sleep
import time
# import for md5
import hashlib
# import for cache
import datetime
from os import path
from os import makedirs
# import for specific round numbers
import math
from os import system

# use official coinbase api
### https://pypi.org/project/coinbase/
### https://github.com/coinbase/coinbase-python/
from coinbase.wallet.client import Client

# globals
g_expire_time = 5

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)

# Init md5 key for cache
g_md5_key = "";
def get_md5_key(json_config:json):
    # print("get_md5_key")
    global g_md5_key

    # read from globals if exist
    if len(g_md5_key) > 0:
        return g_md5_key

    # do it if nothing else exist
    coinbase_api_key = ""
    coinbase_api_secret = ""
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];

    # init globals before return
    g_md5_key = hashlib.md5((coinbase_api_key + "|" + coinbase_api_secret).encode()).hexdigest();
    return g_md5_key
    
# Init coinbase connection
def get_client(json_config:json):
    # print("get_client")
    coinbase_api_key = ""
    coinbase_api_secret = ""
    if "coinbase_api_key" in json_config:
        coinbase_api_key = json_config['coinbase_api_key'];
    if "coinbase_api_secret" in json_config:
        coinbase_api_secret = json_config['coinbase_api_secret'];
    if (coinbase_api_key != "" and coinbase_api_secret != "") :
        return Client(coinbase_api_key, coinbase_api_secret)

# Append all pagined accounts to only one array
g_all_accounts = {}
def get_all_accounts(client: object):
    # print("get_all_accounts")
    global g_all_accounts

    # read from globals if exist
    if len(g_all_accounts) > 0:
        return g_all_accounts

    # read from cache if exist
    if cache_exist("get_all_accounts"):
        g_all_accounts = json.loads(read_from_cache("get_all_accounts"))
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

    # store in cache before return
    store_as_cache(json.dumps(g_all_accounts), "get_all_accounts")

    # return global ...
    return g_all_accounts

# sort transaction by transaction created date reversed
def sort_owned_currencies_by_value(owned_currencies: object):
    return dict(sorted(owned_currencies.items(), key=operator.itemgetter(1), reverse=True))

# get own currencies
g_owned_currencies = {}
def get_owned_currencies(accounts: json):
    # print("get_owned_currencies")
    global g_owned_currencies

    # read from globals if exist
    if len(g_owned_currencies) > 0:
        return g_owned_currencies 

    # read from cache if exist
    if cache_exist("get_owned_currencies"):
        g_owned_currencies = json.loads(read_from_cache("get_owned_currencies"))
        return g_owned_currencies

    # do it if nothing else exist
    owned_currencies = {}
    for currency in accounts:
        balance = float(accounts[currency]['native_balance']['amount'])
        if (balance > 0):
            owned_currencies[currency] = float(accounts[currency]['native_balance']['amount'])

    # init globals before return
    g_owned_currencies = sort_owned_currencies_by_value(owned_currencies);

    # store in cache before return
    store_as_cache(json.dumps(g_owned_currencies), "get_owned_currencies")

    # return global ...
    return g_owned_currencies

# remove transaction tag
def remove_transactions_tag(json_datas: json):
    rule = re.compile(r'<Transaction .*?>')
    str_datas = rule.sub('', json.dumps(json_datas))
    return json.loads(str_datas)

#
def get_all_transactions(client: object, account: str):
    # print("get_all_transactions : " + account)
    all_transactions = []
    starting_after = None
    # infinite loop
    while True:
        transactions = client.get_transactions(account, limit=25, starting_after=starting_after)
        # if pagination exist then push all account in array and loop again
        if transactions.pagination.next_starting_after is not None:
            starting_after = transactions.pagination.next_starting_after
            for transaction in transactions.data:
                transaction = remove_transactions_tag(transaction)
                all_transactions.append(transaction)
            time.sleep(1)
        # if pagination don't exist then push all account in array and exit loop
        else:
            for transaction in transactions.data:
                transaction = remove_transactions_tag(transaction)
                all_transactions.append(transaction)
            break
    return all_transactions

#
g_all_owned_transactions = {}
def get_all_owned_transactions(client: object, owned_currencies: json):
    # print("get_all_owned_transactions")
    global g_all_owned_transactions

    # read from globals if exist
    if len(g_all_owned_transactions) > 0:
        return g_all_owned_transactions 

    # read from cache if exist
    if cache_exist("get_all_owned_transactions"):
        g_all_owned_transactions = json.loads(read_from_cache("get_all_owned_transactions"))
        return g_all_owned_transactions

    # do it if nothing else exist
    if (len(g_all_owned_transactions) > 0):
        return g_all_owned_transactions
    all_owned_transactions = []
    for currency in owned_currencies:
        all_owned_transactions += get_all_transactions(client, currency)

    # init globals before return
    g_all_owned_transactions = all_owned_transactions

    # store in cache before return
    store_as_cache(json.dumps(g_all_owned_transactions), "get_all_owned_transactions")

    # return global ...
    return g_all_owned_transactions

# # how to get and transform created date
# def transactions_created_at(transaction: json):
#     try:
#         print(transaction)
#         return transaction['created_at']
#     except KeyError:
#         return 0

# # sort transaction by transaction created date reversed
# def sort_transaction_by_date(transactions: object):
#     transactions.sort(key=transactions_created_at, reverse=True)
#     return transactions

# sort transaction by transaction created date reversed
def sort_transactions_by_date(transactions: json):
    # print("sort_transactions_by_date")
    transactions.sort(key = lambda x: x['created_at'])
    return transactions
#
def distribute_transactions_at_currency(currencies: json, transactions: json):
    # print("distribute_transactions_at_currency")
    distribute_transactions = {}

    for currency in currencies:
        distribute_transactions[currency] = []
        for transaction in transactions:
            # if 'payment_method_name' in transaction['details']:
            #     if (transaction['details']['payment_method_name'].endswith(currency)):
            #         distribute_transactions[currency].append(transaction)
            if (transaction['amount']['currency'] == currency):
                distribute_transactions[currency].append(transaction)

    return distribute_transactions

def sum_transactions_by_currency(currencies: json, transactions: json):
    # print("sum_transactions_by_currency")
    sum_transactions_by_currency = {}

    for currency in currencies:
        sum_transactions_by_currency[currency] = 0
        for transaction in transactions[currency]:
            sum_transactions_by_currency[currency] += float(transaction['native_amount']['amount'])

    return sum_transactions_by_currency

def diff_currencies_transactions(currencies: json, sum_transactions: json):
    # print("diff_currencies_transactions")
    diff_currencies_transactions = {}

    for currency in currencies:
        diff_currencies_transactions[currency] = math.floor((currencies[currency] - sum_transactions[currency]) * 100) / 100

    return diff_currencies_transactions

def store_as_cache(datas, file_name):
    # print("store_as_cache")

    try:
        if not path.exists('cache'):
            makedirs('cache')
        if not path.exists('cache/' + g_md5_key):
            makedirs('cache/' + g_md5_key)
        path_cache = 'cache/' + g_md5_key + '/' + file_name + '.cache'
        file_datas = open(path_cache, "w").write(datas)
        return True;
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return False;

def cache_exist(file_name):
    # print("cache_exist")

    path_cache = 'cache/' + g_md5_key + '/' + file_name + '.cache'
    if path.exists(path_cache):
        if cache_is_expired(path_cache):
            return False
        return path_cache
    return False;

def cache_is_expired(path_cache):
    # print("cache_is_expired")

    # get file modify date
    modify_date = time.ctime(path.getmtime(path_cache))
    modify_date = datetime.datetime.strptime(modify_date, "%a %b %d %H:%M:%S %Y")
    modify_date = modify_date.timestamp()

    # get current date
    current_date = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
    current_date = current_date.timestamp()

    # if expired return True else False
    if current_date > (modify_date + g_expire_time):
        return True
    return False
        

def read_from_cache(file_name):
    # print("read_from_cache")

    path_cache = cache_exist(file_name)
    if path_cache:
        file_datas = open(path_cache, "r").read()
        return file_datas;
    return "";

looping = True
while looping is True:
    g_all_accounts = {}
    g_owned_currencies = {}
    g_all_owned_transactions = {}

    # Main Script
    g_md5_key = get_md5_key(json_config)
    #print(g_md5_key)
    g_client = get_client(json_config)
    #print(g_client)
    g_all_accounts = get_all_accounts(g_client)
    #print(g_all_accounts)
    g_owned_currencies = get_owned_currencies(g_all_accounts)
    #print(g_owned_currencies)
    g_all_owned_transactions = get_all_owned_transactions(g_client, g_owned_currencies)
    #print(g_all_owned_transactions)
    g_all_ordered_transactions = sort_transactions_by_date(g_all_owned_transactions)
    #print(g_all_ordered_transactions)
    g_all_distributed_transactions = distribute_transactions_at_currency(g_owned_currencies, g_all_ordered_transactions)
    #print(g_all_distributed_transactions)
    g_sum_transaction = sum_transactions_by_currency(g_owned_currencies, g_all_distributed_transactions)
    #print(g_sum_transaction) 
    g_diff_transaction = diff_currencies_transactions(g_owned_currencies, g_sum_transaction)
    # print(g_diff_transaction) 

    system('cls')
    print(g_owned_currencies) 
    print(g_sum_transaction) 
    print(g_diff_transaction) 
    print('{:60}'.format("Total: "))

    time.sleep(15)


# class CoinbaseWalletAuth(AuthBase):
#     def __init__(self, api_key, secret_key):
#         self.api_key = api_key
#         self.secret_key = secret_key
#     def __call__(self, request):
#         timestamp = str(int(time.time()))
#         message = timestamp + request.method + request.path_url + (request.body or "")
#         hmac_key = base64.b64decode(self.secret_key)
#         bitearray = bytearray(self.secret_key, 'utf-8')
#         signature = hmac.new(bitearray, message.encode(), hashlib.sha256).hexdigest()
#         request.headers.update({
#             'CB-ACCESS-KEY': self.api_key,
#             'CB-ACCESS-SIGN': signature,
#             'CB-ACCESS-TIMESTAMP': timestamp,
#             'Content-Type': 'application/json'
#         })
#         return request
# #check all currencies and wallets
# def checker(boolrecord):
#     checkertext=""
#     tot = 0
#     for i in CurrencyList:
#         lookfor = "accounts/"+i
#         r = requests.get(api_url +lookfor, auth=auth)
#         Crypto = str(json.dumps(r.json()["data"]["balance"]["currency"]))
#         Quantity = str(json.dumps(r.json()["data"]["balance"]["amount"]))
#         value = rjson.json()["data"]["rates"][i]
#         conversion = str(round(float(Quantity.strip('"'))/float(value),2))
#         tot = tot + float(conversion)
#         if boolrecord == True:
#             arrowatend = ""
#             if float(comparer[i]) < float(conversion):
#                 arrowatend = "\t\u2191"
#             elif float(comparer[i]) > float(conversion):
#                 arrowatend = "\t\u2193"
#             else:
#                 arrowatend = "\t\u25A0"
#             checkertext = checkertext + Crypto +"\t" + " " +" Quantity: " +"\t"+ str(round(float(Quantity.strip('"')),3)) +"\t" + " EUR: " +"\t" + conversion + arrowatend + "\t" + comparer[i] + "\n"
#         if boolrecord == False:
#             comparer[i] = conversion
#     os.system('cls')
#     return checkertext, tot 
# api_url = 'https://api.coinbase.com/v2/'
#     auth = CoinbaseWalletAuth(API_KEY, API_SECRET)
#     #Check all conversions
#     lookfor = "exchange-rates?currency=EUR"
#     rjson = requests.get(api_url +lookfor, auth=auth)
#     container = checker(boolrecord)
#     print(container[0])
#     print('{:60}'.format("Totale: " + str(round(container[1],2))))
#     boolrecord = True
#     time.sleep(5)