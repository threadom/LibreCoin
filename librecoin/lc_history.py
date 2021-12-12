import json
import requests
from datetime import datetime 
from datetime import timedelta
from datetime import timezone

class lc_history:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_store = self.m_librecoin.store()
        self.m_history = {}

    def get(self, p_currency_from: str, p_currency_to: str, add_day: int, granularity: int = 300):
        # print("lc_get_history")

        currency_pair = p_currency_from + '-' + p_currency_to
        end_date = (datetime.utcnow() + timedelta(days = add_day) - timedelta(hours = 0)).strftime("%Y-%m-%d %H:%M:%S")
        start_date = (datetime.utcnow() + timedelta(days = add_day) - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")
        # print(end_date)
        # print(start_date)
    
        start_time = datetime.timestamp(datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)) - granularity
        end_time = datetime.timestamp(datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc))
        datas = self.m_store.read('lc_history', currency_pair, 'time', start_time, end_time)

        if not datas:
            if add_day < 30:
                url = "https://api.exchange.coinbase.com/products/"+currency_pair+"/candles?granularity=" + str(granularity) + "&start=" + start_date + "&end=" + end_date
                headers = {"Accept": "application/json"}
                response = requests.request("GET", url, headers=headers)
                datas = json.loads(response.text)
                datas_structure = {'time':'integer','low':'real','high':'real','open':'real','close':'real','volume':'real'}
                if 'message' in datas:
                    if datas['message'] == 'NotFound':
                        return {'time':0,'low':0,'high':0,'open':0,'close':0,'volume':0}
            if datas:
                self.m_store.store('lc_history', currency_pair, datas_structure, datas[0])
            else:
                return {'time':0,'low':0,'high':0,'open':0,'close':0,'volume':0}

        id_data = datas[0][0]
        datas = {
            'time': datas[0][0],
            'low': datas[0][1],
            'high': datas[0][2],
            'open': datas[0][3],
            'close': datas[0][4],
            'volume': datas[0][5]
        }
        datas = { id_data : datas }

        if not (currency_pair in self.m_history):
            self.m_history[currency_pair] = {}
        self.m_history[currency_pair] = self.m_history[currency_pair] | datas

        return self.m_history[currency_pair][id_data]