import json
import sys
import time

from librecoin.lc_connection import *
from librecoin.lc_currencies import *
from librecoin.lc_transactions import *
from librecoin.lc_history import *
from librecoin.lc_format import *
from librecoin.lc_cache import *
from librecoin.lc_display import *
from librecoin.lc_keyboard import *
from librecoin.lc_config import *
from librecoin.lc_view import *
from librecoin.lc_thread import *
from librecoin.lc_coinbase import *
from librecoin.lc_store import *

from coinbase.wallet.client import Client

class librecoin:
    def __init__(self, json_config: json):
        self.m_config = False
        self.m_loop = False
        self.m_stop = False

        self.m_connection = False
        self.m_cache = False
        self.m_currencies = False
        self.m_transactions = False
        self.m_display = False
        self.m_keyboard = False
        self.m_view = False
        self.m_thread = False
        self.m_coinbase = False
        self.m_history = False
        self.m_store = False

        self.m_config_path = json_config        
        self.config()

    def config(self):
        if self.m_config:
            return self.m_config

        self.m_config = lc_config(self.m_config_path)
        return self.m_config

    def loop(self):
        if self.m_loop:
            time.sleep(self.config().get("script_sleep"))
            return self.m_loop

        if self.m_stop:
            return False

        self.m_loop = True
        return self.m_loop

    def nothing(self):
        return False

    def coinbase(self):
        if self.m_coinbase:
            return self.m_coinbase

        self.m_coinbase = lc_coinbase(self)
        return self.m_coinbase

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
    
    def store(self):
        if self.m_store:
            return self.m_store

        self.m_store = lc_store(self)
        return self.m_store

    def history(self):
        if self.m_history:
            return self.m_history

        self.m_history = lc_history(self)
        return self.m_history

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

    def keyboard(self):
        if self.m_keyboard:
            return self.m_keyboard

        self.m_keyboard = lc_keyboard(self)
        return self.m_keyboard

    def view(self):
        if self.m_view:
            return self.m_view

        self.m_view = lc_view(self)
        return self.m_view

    def stop(self):
        self.m_stop = True
        self.m_loop = False

    def thread(self):
        if self.m_thread:
            return self.m_thread

        self.m_thread = lc_thread(self)
        return self.m_thread