import threading
import time


class tTransactions(threading.Thread):
    def __init__(self, librecoin: object):
        librecoin.print('tTransactions.init', 7)
        threading.Thread.__init__(self)
        self.m_librecoin = librecoin
        self.m_run = False

    def run(self):
        self.m_librecoin.print('tTransactions.run', 7)
        lc = self.m_librecoin
        loop_time = 60

        self.m_run = True
        while self.m_run:
            begining_time = int(time.time())
            lc.print("begining_time : " + str(begining_time), 8)


            remaining_time = 1
            while remaining_time:
                remaining_time = loop_time - (int(time.time()) - begining_time)
                lc.print("remaining_time : " + str(remaining_time), 9)
                time.sleep(1)
            end_time = int(time.time())
            lc.print("end_time : " + str(end_time), 8)
            elapsed_time = end_time - begining_time
            lc.print("elapsed_time : " + str(elapsed_time), 8)

    def started(self):
        self.m_librecoin.print('tTransactions.started', 10)
        return self.m_run

    def stop(self):
        self.m_librecoin.print('tTransactions.stop', 7)
        self.m_run = False