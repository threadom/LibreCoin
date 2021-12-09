# import keyboard
import curses

class lc_keyboard:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        # self.m_listener = False
        self.m_screen = False
        self.m_terminal = False
        self.m_keys = "  "

    # def listen(self):
    #     keyboard.on_press(self.handle)
            
    # def handle(self, key):
    #     self.m_keys = self.m_keys[1] + key.name
    #     print("\b", end='')

    def press(self, keys: str, callback: str):
        lc = self.m_librecoin
        if self.m_keys.lower() == keys.lower():
            self.m_keys = "  "
            eval(callback)

    def flush(self):
        try:
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()
        except ImportError:
            import sys, termios
            termios.tcflush(sys.stdin, termios.TCIOFLUSH)

    def get_key(self, window):
        if window:
            try:
                key = window.getkey()
            except:
                return False
        return key

    def listen(self):
        if not self.m_terminal:
            if not self.m_screen:
                self.m_screen = curses.initscr()
            if self.m_screen:
                self.m_terminal = self.m_screen.subwin(0, 0)
                self.m_terminal.nodelay(True)
        if self.m_terminal:
            key = self.get_key(self.m_terminal)
            if key:
                self.m_keys = self.m_keys[1] + key
