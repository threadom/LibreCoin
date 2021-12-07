import keyboard

class lc_keyboard:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_listener = False

    def listen(self):
        keyboard.on_press(self.handle)
            
    def handle(self, key):
        print("\b", end='')