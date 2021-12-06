import time
import json
import re 

class lc_transactions:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_all = {}

    ########################################################
    # remove transaction tag
    def __remove_tag(self, json_datas: json):
        rule = re.compile(r'<Transaction .*?>')
        str_datas = rule.sub('', json.dumps(json_datas))
        return json.loads(str_datas)


    ########################################################
    #
    def currency_transactions(self, currency: str):
        print("transactions.currency_transactions : " + currency)

        all_transactions = []
        starting_after = None
        # infinite loop
        while True:
            transactions = self.m_librecoin.connection().get_transactions(currency, limit=25, starting_after=starting_after)
            # if pagination exist then push all account in array and loop again
            if transactions.pagination.next_starting_after is not None:
                starting_after = transactions.pagination.next_starting_after
                for transaction in transactions.data:
                    transaction = self.__remove_tag(transaction)
                    all_transactions.append(transaction)
                time.sleep(1)
            # if pagination don't exist then push all account in array and exit loop
            else:
                for transaction in transactions.data:
                    transaction = self.__remove_tag(transaction)
                    all_transactions.append(transaction)
                break
        return all_transactions


    ########################################################
    #
    def all(self):
        print("transactions.all")

        # read from globals if exist
        if self.m_all:
            return self.m_all 

        # read from cache if exist
        if self.m_librecoin.cache().exist("transactions_all"):
            self.m_all = json.loads(self.m_librecoin.cache().read("transactions_all"))
            return self.m_all

        currencies = self.m_librecoin.currencies().owned_amount()['native']

        # do it if nothing else exist
        if (len(self.m_all) > 0):
            return self.m_all
        all_transactions = []
        for currency in currencies:
            all_transactions += self.currency_transactions(currency)

        # init globals before return
        self.m_all = all_transactions

        # store in cache before return
        self.m_librecoin.cache().store(json.dumps(self.m_all), "transactions_all")

        # return global ...
        return self.m_all


    ########################################################
    # sort transaction by transaction created date reversed
    def sort_transactions_by_date(self, transactions: json):
        # print("sort_transactions_by_date")
        transactions.sort(key = lambda x: x['created_at'])
        return transactions

    ########################################################
    #
    def distributed(self):
        print("transactions.distributed")
        distributed_transactions = {}

        currencies = self.m_librecoin.currencies().owned_amount()['native']
        all_transactions = self.m_librecoin.transactions().all()

        for currency in currencies:
            distributed_transactions[currency] = []
            for transaction in all_transactions:
                # if 'payment_method_name' in transaction['details']:
                #     if (transaction['details']['payment_method_name'].endswith(currency)):
                #         distributed_transactions[currency].append(transaction)
                if (transaction['amount']['currency'] == currency):
                    distributed_transactions[currency].append(transaction)

        return distributed_transactions