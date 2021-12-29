from librecoin.librecoin import librecoin

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ MAIN SCRIPT ~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

lc = librecoin('configs/config.json')
while lc.loop() is True:
    lc.thread().start('threads.datas.tTransactions','tTransactions')
    lc.sleep(1)

lc.stop()