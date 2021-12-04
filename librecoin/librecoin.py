import json

from librecoin.lc_connect import *
from librecoin.lc_history import *
from librecoin.lc_format import *

from coinbase.wallet.client import Client

class librecoin:
    def __init__(self):
        self.m_client = False

    def connect(self, json_config: json):
        if self.m_client: return self.m_client

        self.m_client = lc_connect(json_config)
        return self.m_client

    def history(self, currency_from: str, currency_to: str, add_day: int, granularity: int = 300):
        return lc_history(currency_from, currency_to, add_day, granularity)

    def yesterday(self, currency_from: str, currency_to: str):
        return lc_yesterday(currency_from, currency_to)

    def current(self, currency_from: str, currency_to: str):
        return lc_current(currency_from, currency_to)

    def format(self, number: float):
        return lc_format(number)