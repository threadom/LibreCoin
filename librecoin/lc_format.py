import math

class lc_format:
    def __init__(self, value):
        self.m_value = value

    def auto(self, size: int):       
        value = str(math.floor(self.m_value * 100) / 100).rjust(size)
        return value
