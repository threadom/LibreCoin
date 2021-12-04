import json
import requests
from datetime import datetime 
from datetime import timedelta
from datetime import timezone
from librecoin.lc_store import lc_store

g_lc_history = {}
def lc_history(p_currency_from: str, p_currency_to: str, add_day: int, granularity: int = 300):
    # print("lc_get_history")

    currency_pair = p_currency_from + '-' + p_currency_to
    end_date = (datetime.utcnow() + timedelta(days = add_day) - timedelta(hours = 0)).strftime("%Y-%m-%d %H:%M:%S")
    start_date = (datetime.utcnow() + timedelta(days = add_day) - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")
    # print(end_date)
    # print(start_date)
  
    start_time = datetime.timestamp(datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)) - granularity
    end_time = datetime.timestamp(datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc))
    datas = lc_store.read('lc_history', currency_pair, 'time', start_time, end_time)

    if not datas:
        url = "https://api.exchange.coinbase.com/products/"+currency_pair+"/candles?granularity=" + str(granularity) + "&start=" + start_date + "&end=" + end_date
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers)
        datas = json.loads(response.text)  
        datas_structure = { 'time' : 'integer', 'low' : 'real' , 'high' : 'real', 'open' : 'real', 'close' : 'real', 'volume': 'real' }
        lc_store.store('lc_history', currency_pair, datas_structure, datas[0])

    id_data = datas[0][0];
    datas = {
        'time': datas[0][0],
        'low': datas[0][1],
        'high': datas[0][2],
        'open': datas[0][3],
        'close': datas[0][4],
        'volume': datas[0][5]
    }
    datas = { id_data : datas }

    if not (currency_pair in g_lc_history):
        g_lc_history[currency_pair] = {}
    g_lc_history[currency_pair] = g_lc_history[currency_pair] | datas

    return g_lc_history[currency_pair][id_data]