# Requires python-requests. Install with pip:
#
#   pip install requests
#
# or, with easy-install:
#
#   easy_install requests

import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

class lc_coinbase:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin

    def get(self, url):
        timestamp = str(int(time.time()))
        message = timestamp + "GET" + url
        message = message.encode('utf-8')
        hmac_key = base64.b64decode(self.m_librecoin.config().get('coinbase_api_secret'))
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')

        headers = {
            "Content-Type": "application/json",
            "CB-ACCESS-KEY": self.m_librecoin.config().get("coinbase_api_key"),
            "CA-ACCESS-SIGN": signature_b64,
            "CB-ACCESS-TIMESTAMP": timestamp
        }

        print(headers)
        
        response = requests.request("GET", url, headers=headers)
        
        return response.text

    def get_accounts(self, limit=25, page=1):
        return self.get('https://api.exchange.coinbase.com/accounts')