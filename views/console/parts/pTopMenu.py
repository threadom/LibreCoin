import librecoin

def init(lc:librecoin):
    lc.display().table(0,0,3,3)
    lc.display().hourglass(1,1)
    lc.display().table(2,0,19,3)
    lc.display().ljust("DB:Dashboard", 4, 1, 16)
    lc.display().table(20,0,19,3)
    lc.display().ljust("WL:Wallet", 22, 1, 16)
    lc.display().table(38,0,19,3)
    lc.display().ljust("TS:Transactions", 40, 1, 16)
    lc.display().table(56,0,19,3)
    lc.display().ljust("CH:Crypto Histo", 58, 1, 16)
    lc.display().table(74,0,19,3)
    lc.display().ljust("TR:Trade Rules", 76, 1, 16)
    lc.display().table(92,0,19,3)
    lc.display().ljust("BR:Buy Rules", 94, 1, 16)
    lc.display().table(110,0,19,3)
    lc.display().ljust("SR:Sell Rules", 112, 1, 16)
    lc.display().table(-23,0,13,3)
    lc.display().ljust("CF:Config", -21, 1, 10)
    lc.display().table(-11,0,11,3)
    lc.display().ljust("QQ:Quit", -9, 1, 8)

def update(lc:librecoin):
    lc.display().hourglass(1,1)

def control(lc:librecoin):
    lc.keyboard().press("DB", "lc.view().set('views.console.vDashboard')")
    lc.keyboard().press("WL", "lc.view().set('views.console.vWallet')")
    lc.keyboard().press("TS", "lc.view().set('views.console.vTransactions')")
    lc.keyboard().press("CH", "lc.view().set('views.console.vCryptoHisto')")
    lc.keyboard().press("TR", "lc.view().set('views.console.vTradeRules')")
    lc.keyboard().press("BR", "lc.view().set('views.console.vBuyRules')")
    lc.keyboard().press("SR", "lc.view().set('views.console.vSellRules')")
    lc.keyboard().press("CF", "lc.view().set('views.console.vConfig')")
    lc.keyboard().press("QQ", "lc.view().set('views.console.vQuit')")
