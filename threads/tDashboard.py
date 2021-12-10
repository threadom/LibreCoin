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
                tmp['owned'][currency]['-364'] = lc.history(currency,'EUR', -364, 86400)['close']
                tmp['owned'][currency]['-182'] = lc.history(currency,'EUR', -182, 86400)['close']
                tmp['owned'][currency]['-91'] = lc.history(currency,'EUR', -91, 21600)['close']
                tmp['owned'][currency]['-28'] = lc.history(currency,'EUR', -28, 3600)['close']
                tmp['owned'][currency]['-7'] = lc.history(currency,'EUR', -7, 900)['close']
                tmp['owned'][currency]['-1'] = lc.history(currency,'EUR', -1, 300)['close']
                tmp['owned'][currency]['-0'] = lc.history(currency,'EUR', -0, 60)['close']

            y = 0
            for currency in tmp['owned_amount']:
                y += 1
                lc.display().ljust(currency, 1, y, 9)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-364']).auto(10) + " € |", 10, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-364']).auto(10) + " € |", 20, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-182']).auto(10) + " € |", 30, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-91']).auto(10) + " € |", 40, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-28']).auto(10) + " € |", 50, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-7']).auto(10) + " € |", 60, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-1']).auto(10) + " € |", 70, y, 10)
                lc.display().ljust(lc.format(tmp['owned'][currency]['-0']).auto(10) + " € |", 80, y, 10)

            # self.m_librecoin.display().draw()
            time.sleep(1)

    def stop(self):
        self.m_run = Falsea