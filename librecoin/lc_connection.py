import json

from coinbase.wallet.client import Client

class lc_connection:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_connection = False

    def open(self):
        # print("lc_connect")
        if self.m_connection:
            return self.m_connection
        coinbase_api_key = self.m_librecoin.config().get('coinbase_api_key')
        coinbase_api_secret = self.m_librecoin.config().get('coinbase_api_secret')
        if (coinbase_api_key != "" and coinbase_api_secret != "") :
            self.m_connection = Client(coinbase_api_key, coinbase_api_secret)
            return self.m_connection