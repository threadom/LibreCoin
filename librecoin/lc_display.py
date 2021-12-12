import os


class lc_display:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin

        self.m_screen_width = librecoin.config().get('screen_width')
        self.m_screen_height = librecoin.config().get('screen_height')
        self.m_screen_datas = {}
        self.m_screen_colors = {}
        self.m_screen_bgcolors = {}
        self.m_current_view = False
        self.m_hourglass = False
        self.m_ascii_art = {}
        self.clear()

    def empty(self):
        for x in range(0, self.m_screen_width):
            self.m_screen_datas[x] = {}
            self.m_screen_colors[x] = {}
            self.m_screen_bgcolors[x] = {}
            for y in range(0, self.m_screen_height):
                self.m_screen_datas[x][y] = ' '
                self.m_screen_colors[x][y] = False
                self.m_screen_bgcolors[x][y] = False

    def clear(self):
        # print('clear')
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        old_color = False
        lines = ''
        for y in range(0, self.m_screen_height):
            line = ''
            for x in range(0, self.m_screen_width):
                # Draw Color
                color = ''
                if self.m_screen_colors[x][y]:
                    color = self.m_screen_colors[x][y]
                bgcolor = ''
                if self.m_screen_bgcolors[x][y]:
                    bgcolor = self.m_screen_bgcolors[x][y]
                new_color = self.getColorCode(color, bgcolor)
                if not new_color:
                    new_color = self.getNoColorCode()
                if new_color != old_color:
                    line += new_color
                old_color = new_color
                # Draw Text
                line += self.m_screen_datas[x][y]
            lines += line + '\r\n'
        lines = lines[:-2]
        if old_color != self.getNoColorCode():
            lines += self.getNoColorCode()
        self.zero()
        print(lines, end='')

    def zero(self):
        print('\033[%d;%dH' % (0, 0), end='')

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
            # text = text.ljust(w)
            text = text.ljust(w+1)
            text = text[0:w+1]
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
        for i in range(x+1, x+w):
            # TOP HORIZONTAL LINE
            if self.m_screen_datas[i][y] == chr(int('252C', 16)):
                self.m_screen_datas[i][y] = chr(int('252C', 16))
            elif self.m_screen_datas[i][y] == chr(int('2514', 16)):
                self.m_screen_datas[i][y] = chr(int('2534', 16))
            elif self.m_screen_datas[i][y] == chr(int('2518', 16)):
                self.m_screen_datas[i][y] = chr(int('2534', 16))
            elif self.m_screen_datas[i][y] == chr(int('2534', 16)):
                self.m_screen_datas[i][y] = chr(int('2534', 16))
            else:
                self.m_screen_datas[i][y] = chr(int('2500', 16))

            # BOTTOM HORIZONTAL LINE
            if self.m_screen_datas[i][y+h] == chr(int('2502', 16)):
                self.m_screen_datas[i][y+h] = chr(int('253C', 16))
            else:
                self.m_screen_datas[i][y+h] = chr(int('2500', 16))
        for i in range(y+1, y+h):
            # LEFT VERTICAL LINE
            if self.m_screen_datas[x][i] == chr(int('2524', 16)):
                self.m_screen_datas[x][i] = chr(int('2524', 16))
            else:
                self.m_screen_datas[x][i] = chr(int('2502', 16))
            # RIGHT VERTICAL LINE
            if self.m_screen_datas[x+w][i] == chr(int('2514', 16)):
                self.m_screen_datas[x+w][i] = chr(int('251C', 16))
            elif self.m_screen_datas[x+w][i] == chr(int('251C', 16)):
                self.m_screen_datas[x+w][i] = chr(int('251C', 16))
            else:
                self.m_screen_datas[x+w][i] = chr(int('2502', 16))

        # TOP LEFT CORNER
        if self.m_screen_datas[x][y] == chr(int('2500', 16)):
            self.m_screen_datas[x][y] = chr(int('252C', 16))
        elif self.m_screen_datas[x][y] == chr(int('253C', 16)):
            self.m_screen_datas[x][y] = chr(int('253C', 16))
        elif self.m_screen_datas[x][y] == chr(int('252C', 16)):
            self.m_screen_datas[x][y] = chr(int('252C', 16))
        elif self.m_screen_datas[x][y] == chr(int('251C', 16)):
            self.m_screen_datas[x][y] = chr(int('251C', 16))
        elif self.m_screen_datas[x][y] == chr(int('2520', 16)):
            self.m_screen_datas[x][y] = chr(int('2520', 16))
        elif self.m_screen_datas[x][y] == chr(int('2514', 16)):
            self.m_screen_datas[x][y] = chr(int('251C', 16))
        elif self.m_screen_datas[x][y] == chr(int('2510', 16)):
            self.m_screen_datas[x][y] = chr(int('252C', 16))
        else:
            self.m_screen_datas[x][y] = chr(int('250C', 16))

        # TOP RIGHT CORNER
        if self.m_screen_datas[x+w][y] == chr(int('253C', 16)):
            self.m_screen_datas[x+w][y] = chr(int('253C', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('2502', 16)):
            self.m_screen_datas[x+w][y] = chr(int('2524', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('252C', 16)):
            self.m_screen_datas[x+w][y] = chr(int('252C', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('2500', 16)):
            self.m_screen_datas[x+w][y] = chr(int('252C', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('2524', 16)):
            self.m_screen_datas[x+w][y] = chr(int('2524', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('2518', 16)):
            self.m_screen_datas[x+w][y] = chr(int('2524', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('2534', 16)):
            self.m_screen_datas[x+w][y] = chr(int('253C', 16))
        elif self.m_screen_datas[x+w][y] == chr(int('250C', 16)):
            self.m_screen_datas[x+w][y] = chr(int('252C', 16))
        else:
            self.m_screen_datas[x+w][y] = chr(int('2510', 16))

        # BOTTOM LEFT CORNER
        if self.m_screen_datas[x][y+h] == chr(int('2534', 16)):
            self.m_screen_datas[x][y+h] = chr(int('2534', 16))
        elif self.m_screen_datas[x][y+h] == chr(int('2500', 16)):
            self.m_screen_datas[x][y+h] = chr(int('2534', 16))
        elif self.m_screen_datas[x][y+h] == chr(int('2524', 16)):
            self.m_screen_datas[x][y+h] = chr(int('253C', 16))
        elif self.m_screen_datas[x][y+h] == chr(int('2502', 16)):
            self.m_screen_datas[x][y+h] = chr(int('251C', 16))
        elif self.m_screen_datas[x][y+h] == chr(int('2518', 16)):
            self.m_screen_datas[x][y+h] = chr(int('2534', 16))
        else:
            self.m_screen_datas[x][y+h] = chr(int('2514', 16))

        # BOTTOM RIGHT CORNER
        if self.m_screen_datas[x+w][y+h] == chr(int('2534', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('2534', 16))
        elif self.m_screen_datas[x+w][y+h] == chr(int('251C', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('253C', 16))
        elif self.m_screen_datas[x+w][y+h] == chr(int('2500', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('2534', 16))
        elif self.m_screen_datas[x+w][y+h] == chr(int('2524', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('2524', 16))
        elif self.m_screen_datas[x+w][y+h] == chr(int('2502', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('2524', 16))
        elif self.m_screen_datas[x+w][y+h] == chr(int('2514', 16)):
            self.m_screen_datas[x+w][y+h] = chr(int('2534', 16))
        else:
            self.m_screen_datas[x+w][y+h] = chr(int('2518', 16))

    def hourglass(self, x: int, y: int):
        if x < 0:
            x = (self.m_screen_width + x)
        if y < 0:
            y = (self.m_screen_height + y)

        if self.m_hourglass == chr(int('2557', 16)):
            self.m_hourglass = chr(int('255D', 16))
        elif self.m_hourglass == chr(int('2554', 16)):
            self.m_hourglass = chr(int('2557', 16))
        elif self.m_hourglass == chr(int('255A', 16)):
            self.m_hourglass = chr(int('2554', 16))
        else:
            self.m_hourglass = chr(int('255A', 16))

        self.m_screen_datas[x][y] = self.m_hourglass

    def color(self, color: str, x: int, y: int, w: int, h: int):
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
        # print(x)
        # print(y)
        # print(w)
        # print(h)
        for j in range(y, y+h):
            # print('j'+str(j))
            for i in range(x, x+w):
                # print('i'+str(i))
                self.m_screen_colors[i][j] = color
        # print(self.m_screen_colors)

    def bgcolor(self, bgcolors: str, x: int, y: int, w: int, h: int):
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
        for j in range(y, y+h):
            for i in range(x, x+w):
                self.m_screen_bgcolors[i][j] = bgcolors

    def getNoColorCode(self):
        return '\033[00m'

    def getColorCode(self, color: str, bgcolor: str):
        colorcode = ''
        match color:
            case 'red':
                colorcode += '\033[91m'
            case 'green':
                colorcode += '\033[92m'
            case 'yellow':
                colorcode += '\033[93m'
            case 'blue':
                colorcode += '\033[94m'
            case 'purple':
                colorcode += '\033[95m'
            case 'cyan':
                colorcode += '\033[96m'
            case 'white':
                colorcode += '\033[97m'
            case 'ligthgray':
                colorcode += '\033[37m'
            case 'darkgray':
                colorcode += '\033[90m'
        match bgcolor:
            case 'black':
                colorcode += '\033[40m'
            case 'red':
                colorcode += '\033[41m'
            case 'green':
                colorcode += '\033[42m'
            case 'yellow':
                colorcode += '\033[43m'
            case 'blue':
                colorcode += '\033[44m'
            case 'purple':
                colorcode += '\033[45m'
            case 'cyan':
                colorcode += '\033[46m'
            case 'ligthgray':
                colorcode += '\033[47m'
            case 'darkgray':
                colorcode += '\033[100m'
            case 'white':
                colorcode += '\033[107m'
        if color or bgcolor:
            return colorcode
        return False

    def ascii_art(self, file_path: str, x: int, y: int):
        if not (file_path in self.m_ascii_art):
            self.m_ascii_art[file_path] = {}
            l_file = open(file_path, "r")
            line = l_file.readline()
            j = 0
            while line:
                self.m_ascii_art[file_path][y + j] = {}
                for i, c in enumerate(line):
                    if c != chr(15) and c != chr(10):
                        self.m_ascii_art[file_path][y + j][x + i] = c
                line = l_file.readline()
                j = j + 1
        
        if file_path in self.m_ascii_art:
            for j in self.m_ascii_art[file_path]:
                for i in self.m_ascii_art[file_path][j]:
                    self.m_screen_datas[x+i][y+j] = self.m_ascii_art[file_path][j][i]


