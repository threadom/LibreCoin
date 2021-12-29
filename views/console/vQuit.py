import librecoin

def init(lc:librecoin):
    lc.display().empty()

def update(lc:librecoin):
    lc.display().ascii_art('resources/goodbye.txt', 0, 0)
    lc.keyboard().flush()
    lc.stop()

def control(lc:librecoin):
    lc.keyboard().flush()
