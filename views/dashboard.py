import librecoin

import random

def init(lc:librecoin):
    lc.display().empty()

    lc.view().part("views.parts.top_menu").init()
    lc.display().table(0,2,-0,-0)
    lc.display().table(0,2,-0,3)
    lc.display().ljust("Dashboard", 2, 3, 0)

    lc.display().table(0,4,-0,15)
    lc.display().table(0,4,-29*7,3)
    lc.display().ljust("Wallet History Chart", 2, 5, -29*7)

    # Top5
    def Top5(title:str,x:int,y:int):
        lc.display().table(x-30,y,30,9)
        lc.display().table(x-30,y,30,3)
        lc.display().table(x-11,y+2,11,7)
        lc.display().ljust(title, x-28, y+1, 28)

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
    lc.display().ljust("WE:Wallet Evolution", 2, 19, -29*7)
    lc.display().ljust("Minute Compare", 2, 21, -29*7)

def update(lc:librecoin):
    lc.view().part("views.parts.top_menu").update()

    lc.display().print(str(random.randint(0,99)), 10, 10)

def control(lc:librecoin):
    lc.view().part("views.parts.top_menu").control()
