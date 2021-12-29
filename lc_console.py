from librecoin.librecoin import librecoin

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ MAIN SCRIPT ~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

lc = librecoin('configs/config.json')

lc.display().clear()
lc.view().set("views.console.vDashboard")        
while lc.loop() is True:
    lc.view().display()
    lc.display().draw()
    lc.keyboard().listen()

lc.stop()