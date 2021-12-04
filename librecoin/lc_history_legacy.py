import json
import requests
from datetime import datetime 
from datetime import timedelta

def lc_current(p_currency_from: str, p_currency_to: str):
    # print("lc_current")

    currency_pair = p_currency_from + '-' + p_currency_to

    end_date = (datetime.utcnow() - timedelta(hours = 0)).strftime("%Y-%m-%d %H:%M:%S")
    start_date = (datetime.utcnow() - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")
    print(end_date)
    print(start_date)
    
    url = "https://api.exchange.coinbase.com/products/"+currency_pair+"/candles?granularity=900&start="+start_date+"&end="+end_date
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)

    datas = {}
    if response:
        datas = json.loads(response.text)
        datas = {
            'time': datas[0][0],
            'low': datas[0][1],
            'high': datas[0][2],
            'open': datas[0][3],
            'close': datas[0][4],
            'volume': datas[0][5]
        }

    return datas
    
g_lc_yesterday = {}
def lc_yesterday(p_currency_from: str, p_currency_to: str):
    # print("lc_yesterday")

    currency_pair = p_currency_from + '-' + p_currency_to
    end_date = (datetime.utcnow() - timedelta(days = 1) - timedelta(hours = 0)).strftime("%Y-%m-%d %H:%M:%S")
    start_date = (datetime.utcnow() - timedelta(days = 1) - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")
    print(end_date)
    print(start_date)
    
    url = "https://api.exchange.coinbase.com/products/"+currency_pair+"/candles?granularity=900&start="+start_date+"&end="+end_date
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)

    datas = {}
    if response:
        datas = json.loads(response.text)
        datas = {
            'time': datas[0][0],
            'low': datas[0][1],
            'high': datas[0][2],
            'open': datas[0][3],
            'close': datas[0][4],
            'volume': datas[0][5]
        }

    g_lc_yesterday[currency_pair] = datas
    return g_lc_yesterday[currency_pair]
