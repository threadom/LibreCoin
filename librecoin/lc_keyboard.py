import curses

class lc_keyboard:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        # self.m_listener = False
        self.m_screen = False
        self.m_terminal = False
        self.m_keys = ""

    def press(self, keys: str, callback: str):
        lc = self.m_librecoin
        if self.m_keys.lower() == keys.lower():
            self.m_keys = ""
            eval(callback)

    def flush(self):
        try:
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            import sys, termios
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def get_keys(self, window):
        if window:
            try:
                key = ''
                while True:
                    keys += window.getkey()
            except:
                return False
            curses.flushinp
        return keys

    def listen(self):
        if not self.m_terminal:
            if not self.m_screen:
                self.m_screen = curses.initscr()
            if self.m_screen:
                self.m_terminal = self.m_screen.subwin(0, 0)
                self.m_terminal.nodelay(True)
        if self.m_terminal:
            keys = self.get_keys(self.m_terminal)
            if keys:
                self.m_keys = self.m_keys + keys

