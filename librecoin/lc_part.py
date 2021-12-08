import importlib


class lc_part:
    def __init__(self, librecoin: object, part_name: str):
        self.m_librecoin = librecoin
        self.m_parts = {}

        self.m_part_name = part_name
        self.m_part = False

    def init(self):
        if self.m_part:
            return self.m_part.init(self.m_librecoin)

        self.m_part = importlib.import_module(self.m_part_name)
        return self.m_part.init(self.m_librecoin)

    def update(self):
        if self.m_part:
            return self.m_part.update(self.m_librecoin)

        self.m_part = importlib.import_module(self.m_part_name)
        return self.m_part.update(self.m_librecoin)

    def control(self):
        if self.m_part:
            return self.m_part.control(self.m_librecoin)

        self.m_part = importlib.import_module(self.m_part_name)
        return self.m_part.control(self.m_librecoin)
