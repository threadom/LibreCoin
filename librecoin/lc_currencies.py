import time
import json
import operator
import math

from librecoin.lc_cache import *

class lc_currencies:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_all = False
        self.m_owned_amount = False
        self.m_real_gain = False
        self.m_real_invest = False


    ########################################################
    # get all pagined currencies to only one dict
    def all(self):
        # print("currencies.all")

        # read from globals if exist
        if self.m_all:
            return self.m_all

        # read from cache if exist
        if self.m_librecoin.cache().exist("currencies_all"):
            self.m_all = json.loads(self.m_librecoin.cache().read("currencies_all"))
            return self.m_all

        # do it if nothing else exist
        all_currencies = {}
        starting_after = None
        # infinite loop
        while True:
            accounts = self.m_librecoin.connection().get_accounts(limit=25, starting_after=starting_after)
            # if pagination exist then push all account in array and loop again
            if accounts.pagination.next_starting_after is not None:
                starting_after = accounts.pagination.next_starting_after
                for account in accounts.data:
                    all_currencies[account.currency] = account
                time.sleep(1)
            # if pagination don't exist then push all account in array and exit loop
            else:
                for account in accounts.data:
                    all_currencies[account.currency] = account
                break

        # init globals before return
        self.m_all = all_currencies

        # store in cache before return
        self.m_librecoin.cache().store(json.dumps(self.m_all), "currencies_all")

        # return global ...
        return self.m_all


    ########################################################
    # sort transaction by transaction created date reversed
    def __sort_currencies(self, currencies: object):
        return dict(sorted(currencies.items(), key=operator.itemgetter(1), reverse=True))


    ########################################################
    # get own currencies
    def owned_amount(self):
        # print("currencies.owned_amount")

        # read from globals if exist
        if self.m_owned_amount:
            return self.m_owned_amount 

        # read from cache if exist
        if self.m_librecoin.cache().exist("currencies_owned_amount"):
            self.m_owned_amount = json.loads(self.m_librecoin.cache().read("currencies_owned_amount"))
            return self.m_owned_amount

        currencies = self.all()

        # do it if nothing else exist
        owned_currencies = { 'native': {}, 'crypto': {} }
        for currency in currencies:
            native_amount = float(currencies[currency]['native_balance']['amount'])
            crypto_amount = float(currencies[currency]['balance']['amount'])
            if (native_amount > 0):
                owned_currencies['native'][currency] = float(currencies[currency]['native_balance']['amount'])
                owned_currencies['crypto'][currency] = float(currencies[currency]['balance']['amount'])

        # init globals before return
        owned_currencies['native'] = self.__sort_currencies(owned_currencies['native']);
        owned_currencies['crypto'] = self.__sort_currencies(owned_currencies['crypto']);
        self.m_owned_amount = owned_currencies;

        # store in cache before return
        self.m_librecoin.cache().store(json.dumps(self.m_owned_amount), "currencies_owned_amount")

        # return global ...
        return self.m_owned_amount


    ########################################################
    #
    def real_invest(self):
        # print("currencies.real_invest")
        if self.m_real_invest:
            return self.m_real_invest

        currencies = self.m_librecoin.currencies().owned_amount()['native']
        all_transactions = self.m_librecoin.transactions().distributed()
        
        real_invest = { 'native': {}, 'crypto': {} }
        for currency in currencies:
            real_invest['native'][currency] = 0
            real_invest['crypto'][currency] = 0
            for transaction in all_transactions[currency]:
                real_invest['native'][currency] += float(transaction['native_amount']['amount'])
                real_invest['crypto'][currency] += float(transaction['amount']['amount'])

        self.m_real_invest = real_invest
        return self.m_real_invest


    ########################################################
    #
    def real_gain(self):
        # print("currencies.real_gain")
        if self.m_real_gain:
            return self.m_real_gain

        real_gain = { 'native': {}, 'crypto': {} }

        currencies = self.m_librecoin.currencies().owned_amount()['native']
        real_invest = self.m_librecoin.currencies().real_invest()['native']
        for currency in currencies:
            real_gain['native'][currency] = math.floor((currencies[currency] - real_invest[currency]) * 100) / 100

        currencies = self.m_librecoin.currencies().owned_amount()['crypto']
        real_invest = self.m_librecoin.currencies().real_invest()['crypto']
        for currency in currencies:
            real_gain['crypto'][currency] = math.floor((currencies[currency] - real_invest[currency]) * 100) / 100

        self.m_real_gain = real_gain
        return self.m_real_gain