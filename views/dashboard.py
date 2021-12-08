import librecoin

import random

def init(lc:librecoin):
    lc.display().empty()

    lc.view().part("views.parts.top_menu").init()
    lc.display().table(0,2,-0,-0)
    lc.display().table(0,2,-0,3)
    lc.display().ljust("Dashboard", 2, 3, -1)

    lc.display().table(0,4,-0,15)
    lc.display().table(0,4,-29*7,3)
    lc.display().ljust("Wallet History Chart", 2, 5, -29*7-1)
    lc.display().color('red', 2, 5, -29*7-1, 1)
    
    # lc.display().ljust("Wallet History Chart", 2, 7, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 8, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 9, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 10, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 11, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 12, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 13, -29*7-1)
    # lc.display().ljust("Wallet History Chart", 2, 14, -29*7-1)

    # lc.display().color('red', 2, 7, -29*7-1, 1)
    # lc.display().color('green', 2, 8, -29*7-1, 1)
    # lc.display().color('yellow', 2, 9, -29*7-1, 1)
    # lc.display().color('blue', 2, 10, -29*7-1, 1)
    # lc.display().color('purple', 2, 11, -29*7-1, 1)
    # lc.display().color('cyan', 2, 12, -29*7-1, 1)
    # lc.display().color('white', 2, 13, -29*7-1, 1)
    # lc.display().color('gray', 2, 14, -29*7-1, 1)

    # lc.display().bgcolor('red', -29*7, 7, -29*6-1, 1)
    # lc.display().bgcolor('green', -29*7, 8, -29*6-1, 1)
    # lc.display().bgcolor('yellow', -29*7, 9, -29*6-1, 1)
    # lc.display().bgcolor('blue', -29*7, 10, -29*6-1, 1)
    # lc.display().bgcolor('purple', -29*7, 11, -29*6-1, 1)
    # lc.display().bgcolor('cyan', -29*7, 12, -29*6-1, 1)
    # lc.display().bgcolor('gray', -29*7, 13, -29*6-1, 1)
    # lc.display().bgcolor('black', -29*7, 14, -29*6-1, 1)
    
    # Top5
    def Top5(title:str,x:int,y:int):
        lc.display().table(x-30,y,30,9)
        lc.display().table(x-30,y,30,3)
        lc.display().table(x-11,y+2,11,7)
        lc.display().ljust(title, x-28, y+1, 27)

    Top5("Top 5 Increase - Yearly", -29*6, 18)
    Top5("Top 5 Decrease - Yearly", -29*6, 26)
    Top5("Top 5 Increase - Monthly", -29*5, 18)
    Top5("Top 5 Decrease - Monthly", -29*5, 26)
    Top5("Top 5 Increase - Daily", -29*4, 18)
    Top5("Top 5 Decrease - Daily", -29*4, 26)
    Top5("Top 5 Increase - Hourly", -29*3, 18)
    Top5("Top 5 Decrease - Hourly", -29*3, 26)
    Top5("Top 5 Increase - 15 min", -29*2, 18)
    Top5("Top 5 Decrease - 15 min", -29*2, 26)
    Top5("Top 5 Increase - 5 min", -29, 18)
    Top5("Top 5 Decrease - 5 min", -29, 26)
    Top5("Top 5 Increase - 1 min", 0, 18)
    Top5("Top 5 Decrease - 1 min", 0, 26)

    # Wallet Evolution
    lc.display().table(0, 18, -29*7, 0)
    lc.display().table(0, 18, -29*7, 3)
    lc.display().table(0, 20, -29*7, 3)
    lc.display().table(-29*7 -9, 22, 7, 0)
    lc.display().table(-29*7 -3, 22, 3, 0)
    lc.display().ljust("WE:Wallet Evolution", 2, 19, -29*7-1)
    lc.display().ljust("Minute Compare", 2, 21, -29*7-1)

def update(lc:librecoin):
    lc.view().part("views.parts.top_menu").update()

    # lc.display().print(str(random.randint(0,99)), 10, 10)

def control(lc:librecoin):
    lc.view().part("views.parts.top_menu").control()
