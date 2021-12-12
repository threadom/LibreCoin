import threading
import time


class tDashboard(threading.Thread):
    def __init__(self, librecoin: object):
        threading.Thread.__init__(self)
        self.m_librecoin = librecoin
        self.m_run = True

    def run(self):
        lc = self.m_librecoin

        i = 0        
        while self.m_run:
            # print("thread"+str(i))
            i += 1
            self.m_librecoin.display().ljust("thread:"+str(i), 10, 10, 10)

            tmp = {}
            tmp['owned_amount'] = lc.currencies().owned_amount()['native']
            # tmp['real_invest'] = lc.currencies().real_invest()['native']
            # tmp['real_gain'] = lc.currencies().real_gain()['native']
            tmp['owned'] = {}
            for currency in tmp['owned_amount']:
                tmp['owned'][currency] = {}
                tmp['owned'][currency]['-7'] = lc.history().get(currency,'EUR', -7, 60)['close']
                tmp['owned'][currency]['-6'] = lc.history().get(currency,'EUR', -6, 60)['close']
                tmp['owned'][currency]['-5'] = lc.history().get(currency,'EUR', -5, 60)['close']
                tmp['owned'][currency]['-4'] = lc.history().get(currency,'EUR', -4, 60)['close']
                tmp['owned'][currency]['-3'] = lc.history().get(currency,'EUR', -3, 60)['close']
                tmp['owned'][currency]['-2'] = lc.history().get(currency,'EUR', -2, 60)['close']
                tmp['owned'][currency]['-1'] = lc.history().get(currency,'EUR', -1, 60)['close']
                tmp['owned'][currency]['-0'] = lc.history().get(currency,'EUR', -0, 60)['close']

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-6/-7%'] = ((tmp['owned'][currency]['-6'] / tmp['owned'][currency]['-7']) * 100) - 100
                else:
                    tmp['owned'][currency]['-6/-7%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-5/-6%'] = ((tmp['owned'][currency]['-5'] / tmp['owned'][currency]['-6']) * 100) - 100
                else:
                    tmp['owned'][currency]['-5/-6%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-4/-5%'] = ((tmp['owned'][currency]['-4'] / tmp['owned'][currency]['-5']) * 100) - 100
                else:
                    tmp['owned'][currency]['-4/-5%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-3/-4%'] = ((tmp['owned'][currency]['-3'] / tmp['owned'][currency]['-4']) * 100) - 100
                else:
                    tmp['owned'][currency]['-3/-4%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-2/-3%'] = ((tmp['owned'][currency]['-2'] / tmp['owned'][currency]['-3']) * 100) - 100
                else:
                    tmp['owned'][currency]['-2/-3%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-1/-2%'] = ((tmp['owned'][currency]['-1'] / tmp['owned'][currency]['-2']) * 100) - 100
                else:
                    tmp['owned'][currency]['-1/-2%'] = ""

                if tmp['owned'][currency]['-0'] > 0:
                    tmp['owned'][currency]['-0/-1%'] = ((tmp['owned'][currency]['-0'] / tmp['owned'][currency]['-1']) * 100) - 100
                else:
                    tmp['owned'][currency]['-0/-1%'] = ""

            y = 23
            for currency in tmp['owned_amount']:
                lc.display().ljust(currency, 2, y, 8)
                lc.display().color('white', 2, y, 8, 1)
                lc.display().bgcolor('blue', 2, y, 8, 1)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-6/-7%']).auto(8) + " %", 13, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-5/-6%']).auto(8) + " %", 25, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-4/-5%']).auto(8) + " %", 37, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-3/-4%']).auto(8) + " %", 49, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-2/-3%']).auto(8) + " %", 61, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-1/-2%']).auto(8) + " %", 73, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-0/-1%']).auto(8) + " %", 85, y, 10)
                lc.display().color('white', 13, y, 10, 1)
                lc.display().bgcolor('blue', 13, y, 10, 1)
                y += 1
            # self.m_librecoin.display().draw()
            time.sleep(10)

    def stop(self):
        self.m_run = False