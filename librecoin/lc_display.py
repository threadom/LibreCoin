import os

class lc_display:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin

        self.m_screen_width = librecoin.m_json_config['screen_width']
        self.m_screen_height = librecoin.m_json_config['screen_height']
        self.m_screen_datas = {}
        for x in range(0,self.m_screen_width):
            self.m_screen_datas[x] = {}
            for y in range(0,self.m_screen_height):    
                self.m_screen_datas[x][y] = "#"

    def clear(self):
        for x in range(0,self.m_screen_width):
            self.m_screen_datas[x] = {}
            for y in range(0,self.m_screen_height):    
                self.m_screen_datas[x][y] = "#"

    def draw(self):
        lines = ""
        for x in range(0,self.m_screen_width):
            line = ""
            for y in range(0,self.m_screen_height):    
                line += self.m_screen_datas[x][y]
            lines += line
        os.system('cls' if os.name=='nt' else 'clear')
        print(lines)
