import librecoin

def init(lc:librecoin):
    lc.display().table(0,0,3,3)
    lc.display().hourglass(1,1)
    lc.display().table(2,0,19,3)
    lc.display().print(" DB:Dashboard    ", 3, 1)
    lc.display().table(20,0,19,3)
    lc.display().print(" WL:Wallet       ", 21, 1)
    lc.display().table(38,0,19,3)
    lc.display().print(" TS:Transactions ", 39, 1)
    lc.display().table(56,0,19,3)
    lc.display().print(" CH:Crypto Histo ", 57, 1)
    lc.display().table(74,0,19,3)
    lc.display().print(" TR: Trade Rules ", 75, 1)
    lc.display().table(92,0,19,3)
    lc.display().print(" BR: Buy Rules   ", 93, 1)
    lc.display().table(110,0,19,3)
    lc.display().print(" SR: Sell Rules  ", 111, 1)
    lc.display().table(-25,0,14,3)
    lc.display().print(" CF: Config ", -24, 1)
    lc.display().table(-12,0,12,3)
    lc.display().print(" QQ: Quit ", -11, 1)

def update(lc:librecoin):
    lc.display().hourglass(1,1)

def control(lc:librecoin):
    lc.keyboard().press("DB", "lc.view().set('views.dashboard')")
    lc.keyboard().press("WL", "lc.view().set('views.wallet')")
    lc.keyboard().press("TS", "lc.view().set('views.transactions')")
    lc.keyboard().press("CH", "lc.view().set('views.crypto_histo')")
    lc.keyboard().press("TR", "lc.view().set('views.trade_rules')")
    lc.keyboard().press("BR", "lc.view().set('views.buy_rules')")
    lc.keyboard().press("SR", "lc.view().set('views.sell_rules')")
    lc.keyboard().press("CF", "lc.view().set('views.config')")
    lc.keyboard().press("QQ", "lc.view().set('views.quit')")
