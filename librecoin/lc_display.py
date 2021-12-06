import os

class lc_display:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin

        self.m_screen_width = librecoin.m_json_config['screen_width']
        self.m_screen_height = librecoin.m_json_config['screen_height']
        self.m_screen_datas = {}
        self.clear()

    def clear(self):
        for x in range(0,self.m_screen_width):
            self.m_screen_datas[x] = {}
            for y in range(0,self.m_screen_height):    
                self.m_screen_datas[x][y] = " "
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        lines = ""
        for y in range(0,self.m_screen_height):    
            line = ""
            for x in range(0,self.m_screen_width):
                line += self.m_screen_datas[x][y]
            lines += line
        self.zero()
        print(lines)

    def zero(self):
        print("\033[%d;%dH" % (0, 0))

    def print(self, text: str, x: int, y: int):
        if x < 0 or x > self.m_screen_width:
            return False
        if y < 0 or y > self.m_screen_height:
            return False
        if text:
            for i, c in enumerate(text):
                self.m_screen_datas[x + i][y] = c

    def table(self, x: int, y: int, w: int, h: int):
        w = w - 1
        h = h - 1
        for i in range(x,x+w):
            self.m_screen_datas[i][y] = chr(int("2500",16))
            self.m_screen_datas[i][y+h] = chr(int("2500",16))
        for i in range(y,h):
            self.m_screen_datas[x][i] = chr(int("2502",16))
            self.m_screen_datas[x+w][i] = chr(int("2502",16))
        self.m_screen_datas[x][y] = chr(int("250C",16))
        self.m_screen_datas[x+w][y] = chr(int("2510",16))
        self.m_screen_datas[x][y+h] = chr(int("2514",16))
        self.m_screen_datas[x+w][y+h] = chr(int("2518",16))
