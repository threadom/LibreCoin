import librecoin

def main(lc:librecoin):
    lc.display().empty()

    lc.view().part("views.parts.top_menu")
    lc.display().table(0,2,-0,-0)
    lc.display().table(0,2,-0,3)
    lc.display().ljust(" Wallet ", 1, 3, 0)