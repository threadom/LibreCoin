import librecoin

def main(lc:librecoin):
    lc.view().part("views.parts.top_menu")
    lc.display().table(0,2,16,3)
    lc.display().print(" Menu 1       ", 1, 3)
    