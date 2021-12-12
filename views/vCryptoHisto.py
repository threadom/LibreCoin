import librecoin

def init(lc:librecoin):
    lc.display().empty()
    
    lc.view().part("parts.pTopMenu").init()
    lc.display().table(0,2,-0,-0)
    lc.display().table(0,2,-0,3)
    lc.display().ljust(" Crypto Histo ", 1, 3, 0)

def update(lc:librecoin):
    lc.view().part("parts.pTopMenu").update()

def control(lc:librecoin):
    lc.view().part("parts.pTopMenu").control()
