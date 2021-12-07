import json
import sys

from librecoin.lc_connection import *
from librecoin.lc_currencies import *
from librecoin.lc_transactions import *
from librecoin.lc_history import *
from librecoin.lc_format import *
from librecoin.lc_cache import *
from librecoin.lc_display import *
from librecoin.lc_keyboard import *

from coinbase.wallet.client import Client

class librecoin:
    def __init__(self, json_config: json):
        self.m_json_config = json_config
        self.m_connection = False
        self.m_cache = False
        self.m_currencies = False
        self.m_transactions = False
        self.m_display = False
        self.m_keyboard = False

    def connection(self):
        if self.m_connection:
            return self.m_connection

        self.m_connection = lc_connection(self).open()
        return self.m_connection

    def cache(self):
        if self.m_cache:
            return self.m_cache

        self.m_cache = lc_cache(self)
        return self.m_cache

    def currencies(self):
        if self.m_currencies:
            return self.m_currencies

        self.m_currencies = lc_currencies(self)
        return self.m_currencies

    def transactions(self):
        if self.m_transactions:
            return self.m_transactions

        self.m_transactions = lc_transactions(self)
        return self.m_transactions

    def history(self, currency_from: str, currency_to: str, add_day: int, granularity: int = 300):
        return lc_history(currency_from, currency_to, add_day, granularity)

    def yesterday(self, currency_from: str, currency_to: str):
        return lc_yesterday(currency_from, currency_to)

    def current(self, currency_from: str, currency_to: str):
        return lc_current(currency_from, currency_to)

    def format(self, number: float):
        return lc_format(number)

    def divide(self, number1, number2):
        if type(number1) is str:
            return ""
        if type(number2) is str:
            return ""
        if number2 == 0:
            return ""
        return number1 / number2

    def percent(self, number1, number2, digit: int=2):
        if type(number1) is str:
            return ""
        if type(number2) is str:
            return ""
        if number2 == 0:
            return ""
        # return round((number1 / number2 * 100) / (10 ** digit)) * (10 ** digit)
        return round((number1 / number2) * 100)  

    def sub(self, number1, number2):
        if type(number1) is str:
            return ""
        if type(number2) is str:
            return ""
        return number1 - number2

    def display(self):
        if self.m_display:
            return self.m_display

        self.m_display = lc_display(self)
        return self.m_display

    def config(self, property_name):
        if property_name in self.m_json_config:
            return self.m_json_config[property_name]
        print("Missing property '" + property_name + "' in config.json")
        sys.exit()

    def keyboard(self):
        if self.m_keyboard:
            return self.m_keyboard

        self.m_keyboard = lc_keyboard(self)
        return self.m_keyboard