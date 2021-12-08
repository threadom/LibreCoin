import importlib

from librecoin.lc_part import *

class lc_view:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_current_view = False
        self.m_views = {}
        self.m_parts = {}
        self.m_init = False

    def set(self, view_name: str):
        self.m_init = True
        self.m_current_view = view_name
        if not (view_name in self.m_views):
            self.m_views[view_name] = importlib.import_module(view_name)

    def display(self):
        if not (self.m_current_view in self.m_views):
            return False

        self.m_views[self.m_current_view].control(self.m_librecoin)
        if self.m_init:
            self.m_init = False
            self.m_views[self.m_current_view].init(self.m_librecoin)
        self.m_views[self.m_current_view].update(self.m_librecoin)

    def part(self, part_name: str):
        if part_name in self.m_parts:
            return self.m_parts[part_name]

        self.m_parts[part_name] = lc_part(self.m_librecoin, part_name)
        return self.m_parts[part_name]