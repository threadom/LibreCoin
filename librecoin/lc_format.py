import math

class lc_format:
    def __init__(self, value):
        self.m_value = value

    def auto(self, size: int, symbol: str=""):
        value = ""
        if self.m_value == "":
            return "".rjust(size)
        if type(self.m_value) is str:
            value = self.m_value.rjust(size)
        if type(self.m_value) is int:
            value = (str(math.floor(self.m_value * 100) / 100) + symbol).rjust(size)
        if type(self.m_value) is float:
            value = (str(math.floor(self.m_value * 100) / 100) + symbol).rjust(size) 
        return value
