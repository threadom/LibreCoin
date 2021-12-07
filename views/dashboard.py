import librecoin

def main(lc:librecoin):
    lc.display().empty()

    lc.view().part("views.parts.top_menu")
    lc.display().table(0,2,-0,-0)
    lc.display().table(0,2,-0,3)
    lc.display().ljust(" Dashboard ", 1, 3, 0)

    lc.display().table(0,4,-0,15)
    lc.display().table(0,4,24,3)
    lc.display().print(" Wallet History Chart ", 1, 5)

    lc.display().table(0,18,30,9)
    lc.display().table(0,18,30,3)
    lc.display().table(19,20,11,7)
    lc.display().ljust(" Top 5 Increase - Yearly", 1, 19, 29)
    lc.display().table(0,26,30,9)
    lc.display().table(0,26,30,3)
    lc.display().table(19,28,11,7)
    lc.display().ljust(" Top 5 Decrease - Yearly ", 1, 27, 29)

    lc.display().table(29,18,30,9)
    lc.display().table(29,18,30,3)
    lc.display().table(48,20,11,7)
    lc.display().ljust(" Top 5 Increase - Monthly ", 30, 19, 29)
    lc.display().table(29,26,30,9)
    lc.display().table(29,26,30,3)
    lc.display().table(48,28,11,7)
    lc.display().ljust(" Top 5 Decrease - Monthly ", 30, 27, 29)

    lc.display().table(58,18,30,9)
    lc.display().table(58,18,30,3)
    lc.display().table(77,20,11,7)
    lc.display().ljust(" Top 5 Increase - Daily ", 59, 19, 29)
    lc.display().table(58,26,30,9)
    lc.display().table(58,26,30,3)
    lc.display().table(77,28,11,7)
    lc.display().ljust(" Top 5 Decrease - Daily ", 59, 27, 29)

    lc.display().table(87,18,30,9)
    lc.display().table(87,18,30,3)
    lc.display().table(106,20,11,7)
    lc.display().ljust(" Top 5 Increase - Hourly ", 88, 19, 29)
    lc.display().table(87,26,30,9)
    lc.display().table(87,26,30,3)
    lc.display().table(106,28,11,7)
    lc.display().ljust(" Top 5 Decrease - Hourly ", 88, 27, 29)