from pynput import keyboard

class lc_keyboard:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_listener = False

    def listen(self):
        self.m_listener = keyboard.Listener(on_press=self.handle)
        self.m_listener.start()
            
    def handle(self, key):
        print("\b", end='')

    def stop(self):
        self.m_listener.stop()