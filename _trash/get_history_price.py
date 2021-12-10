# import JSON
import json

from librecoin.librecoin import librecoin


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ MAIN SCRIPT ~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)
   
# get Client connection key
lc = librecoin()
# lc.connect(json_config)

currency = "SHIB"
# for currency in lc.owned_currencies():
   # print(lc.amount(currency))
   # print(lc.investissment(currency))
   # print(lc.gain(currency))
print(lc.history(currency,'EUR', -9)['close'])
print(lc.history(currency,'EUR', -8)['close'])
print(lc.history(currency,'EUR', -7)['close'])
print(lc.history(currency,'EUR', -6)['close'])
print(lc.history(currency,'EUR', -5)['close'])
print(lc.history(currency,'EUR', -4)['close'])
print(lc.history(currency,'EUR', -3)['close'])
print(lc.history(currency,'EUR', -2)['close'])
print(lc.history(currency,'EUR', -1)['close'])
print(lc.history(currency,'EUR', -0)['close'])
# print(lc.yesterday(currency,'EUR')['close'])
# print(lc.current(currency,'EUR')['close'])
