# import JSON
import json
# import for sort (and filters)
import re 
import operator
# import for sleep
import time
# import for cache
import datetime
from os import path
from os import makedirs
# import for specific round numbers
import math
import os

# use official coinbase api
### https://pypi.org/project/coinbase/
### https://github.com/coinbase/coinbase-python/
from coinbase.wallet.client import Client

from librecoin.librecoin import librecoin


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ MAIN SCRIPT ~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Loading configuration
with open('config.json') as datas_config:
   json_config = json.load(datas_config)

lc = librecoin(json_config)

looping = True
while looping is True:
    # draw screen
    lc.display().draw()
    time.sleep(1)
