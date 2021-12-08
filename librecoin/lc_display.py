import os

class lc_display:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin

        self.m_screen_width = librecoin.config().get('screen_width')
        self.m_screen_height = librecoin.config().get('screen_height')
        self.m_screen_datas = {}
        self.m_current_view = False
        self.m_hourglass = False
        self.clear()

    def empty(self):
        for x in range(0,self.m_screen_width):
            self.m_screen_datas[x] = {}
            for y in range(0,self.m_screen_height):    
                self.m_screen_datas[x][y] = " "

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        lines = ""
        for y in range(0,self.m_screen_height):    
            line = ""
            for x in range(0,self.m_screen_width):
                line += self.m_screen_datas[x][y]
            lines += line + "\r\n"
        lines = lines[:-2]
        self.zero()
        print(lines, end = '')

    def zero(self):
        print("\033[%d;%dH" % (0, 0))

    def print(self, text: str, x: int, y: int):
        if x < 0:
            x = self.m_screen_width + x
        if y < 0:
            y = self.m_screen_height + y
        if x < 0 or x > self.m_screen_width:
            return False
        if y < 0 or y > self.m_screen_height:
            return False
        if text:
            for i, c in enumerate(text):
                self.m_screen_datas[x + i][y] = c

    def ljust(self, text: str, x: int, y: int, w: int):
        if x < 0:
            x = self.m_screen_width + x
        if y < 0:
            y = self.m_screen_height + y
        if w == 0:
            w = self.m_screen_width - x
        if w < 0:
            w = self.m_screen_width - x + w
        w = w - 1
        if x < 0 or x > self.m_screen_width:
            return False
        if y < 0 or y > self.m_screen_height:
            return False
        if text:
            text = text.ljust(w)
            # text = text.ljust(w,'.')
            for i, c in enumerate(text):
                self.m_screen_datas[x + i][y] = c

    def table(self, x: int, y: int, w: int, h: int):
        if x < 0:
            x = (self.m_screen_width + x)
        if y < 0:
            y = (self.m_screen_height + y)
        if w == 0:
            w = self.m_screen_width - x
        if h == 0:
            h = self.m_screen_height - y
        if w < 0:
            w = self.m_screen_width - x + w
        if h < 0:
            h = self.m_screen_height - x + h
        w = w - 1
        h = h - 1

        # CHARCODE ON https://en.wikipedia.org/wiki/Box-drawing_character
        for i in range(x+1,x+w):
            # TOP HORIZONTAL LINE
            if self.m_screen_datas[i][y] == chr(int("252C",16)):
                self.m_screen_datas[i][y] = chr(int("252C",16))
            elif self.m_screen_datas[i][y] == chr(int("2514",16)):
                self.m_screen_datas[i][y] = chr(int("2534",16))
            elif self.m_screen_datas[i][y] == chr(int("2518",16)):
                self.m_screen_datas[i][y] = chr(int("2534",16))
            elif self.m_screen_datas[i][y] == chr(int("2534",16)):
                self.m_screen_datas[i][y] = chr(int("2534",16))
            else:
                self.m_screen_datas[i][y] = chr(int("2500",16))

            # BOTTOM HORIZONTAL LINE
            if self.m_screen_datas[i][y+h] == chr(int("2502",16)):
                self.m_screen_datas[i][y+h] = chr(int("253C",16))
            else:
                self.m_screen_datas[i][y+h] = chr(int("2500",16))
        for i in range(y+1,y+h):
            # VERTICAL LINE
            if self.m_screen_datas[x][i] == chr(int("2524",16)):
                self.m_screen_datas[x][i] = chr(int("2524",16))
            else:
                self.m_screen_datas[x][i] = chr(int("2502",16))
            self.m_screen_datas[x+w][i] = chr(int("2502",16))

        # TOP LEFT CORNER
        if self.m_screen_datas[x][y] == chr(int("2500",16)):
            self.m_screen_datas[x][y] = chr(int("252C",16))
        elif self.m_screen_datas[x][y] == chr(int("253C",16)):
            self.m_screen_datas[x][y] = chr(int("253C",16))
        elif self.m_screen_datas[x][y] == chr(int("252C",16)):
            self.m_screen_datas[x][y] = chr(int("252C",16))
        elif self.m_screen_datas[x][y] == chr(int("251C",16)):
            self.m_screen_datas[x][y] = chr(int("251C",16))
        elif self.m_screen_datas[x][y] == chr(int("2520",16)):
            self.m_screen_datas[x][y] = chr(int("2520",16))
        elif self.m_screen_datas[x][y] == chr(int("2514",16)):
            self.m_screen_datas[x][y] = chr(int("251C",16))
        elif self.m_screen_datas[x][y] == chr(int("2510",16)):
            self.m_screen_datas[x][y] = chr(int("252C",16))
        else:
            self.m_screen_datas[x][y] = chr(int("250C",16))

        # TOP RIGHT CORNER  
        if self.m_screen_datas[x+w][y] == chr(int("252C",16)):
            self.m_screen_datas[x+w][y] = chr(int("252C",16))
        elif self.m_screen_datas[x+w][y] == chr(int("2500",16)):
            self.m_screen_datas[x+w][y] = chr(int("252C",16))
        elif self.m_screen_datas[x+w][y] == chr(int("2524",16)):
            self.m_screen_datas[x+w][y] = chr(int("2524",16))
        elif self.m_screen_datas[x+w][y] == chr(int("2518",16)):
            self.m_screen_datas[x+w][y] = chr(int("2524",16))
        elif self.m_screen_datas[x+w][y] == chr(int("2534",16)):
            self.m_screen_datas[x+w][y] = chr(int("253C",16))
        elif self.m_screen_datas[x+w][y] == chr(int("250C",16)):
            self.m_screen_datas[x+w][y] = chr(int("252C",16))    
        else:
            self.m_screen_datas[x+w][y] = chr(int("2510",16))

        # BOTTOM LEFT CORNER
        if self.m_screen_datas[x][y+h] == chr(int("2500",16)):
            self.m_screen_datas[x][y+h] = chr(int("2534",16))    
        elif self.m_screen_datas[x][y+h] == chr(int("2524",16)):
            self.m_screen_datas[x][y+h] = chr(int("253C",16))    
        elif self.m_screen_datas[x][y+h] == chr(int("2502",16)):
            self.m_screen_datas[x][y+h] = chr(int("251C",16))    
        elif self.m_screen_datas[x][y+h] == chr(int("2518",16)):
            self.m_screen_datas[x][y+h] = chr(int("2534",16))    
        else:
            self.m_screen_datas[x][y+h] = chr(int("2514",16))

        # BOTTOM RIGHT CORNER
        if self.m_screen_datas[x+w][y+h] == chr(int("2502",16)):
            self.m_screen_datas[x+w][y+h] = chr(int("2524",16))    
        elif self.m_screen_datas[x+w][y+h] == chr(int("2514",16)):
            self.m_screen_datas[x+w][y+h] = chr(int("2534",16))    
        else:
            self.m_screen_datas[x+w][y+h] = chr(int("2518",16))

    def hourglass(self, x: int, y: int):
        if x < 0:
            x = (self.m_screen_width + x)
        if y < 0:
            y = (self.m_screen_height + y)

        if self.m_hourglass == chr(int("2557",16)):
            self.m_hourglass = chr(int("255D",16))
        elif self.m_hourglass == chr(int("2554",16)):
            self.m_hourglass = chr(int("2557",16))
        elif self.m_hourglass == chr(int("255A",16)):
            self.m_hourglass = chr(int("2554",16))
        else:
            self.m_hourglass = chr(int("255A",16))
        
        self.m_screen_datas[x][y] = self.m_hourglass