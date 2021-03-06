import os 

class lc_keyboard:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_listener = False
        self.m_screen = False
        self.m_terminal = False
        self.m_keys = "  "

    def on_press(self, key):
        try:
            key = key.char
        except:
            return False

        self.m_keys = self.m_keys[-1] + key

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

    def get_keys(self, window):
        if window:
            keys = ''
            try:
                while True:
                    keys += window.getkey()
            except:
                # curses.flushinp
                if keys:
                    return keys
                return False
        return False

    def listen(self):
        if os.name == 'nt':
            if not self.m_listener:
                from pynput import keyboard

                self.m_listener = keyboard.Listener(on_press=self.on_press)
                self.m_listener.start()
        else:
            if not self.m_terminal:
                import curses
                if not self.m_screen:
                    self.m_screen = curses.initscr()
                if self.m_screen:
                    self.m_terminal = self.m_screen.subwin(0, 0)
                    self.m_terminal.nodelay(True)

            if self.m_terminal:
                keys = self.get_keys(self.m_terminal)
                if keys:
                    if len(keys) > 1:
                        self.m_keys = keys[0:2]
                    if len(keys) > 0:
                        self.m_keys = self.m_keys[-1] + keys[0:1]

