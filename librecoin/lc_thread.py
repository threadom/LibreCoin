from importlib import import_module

from librecoin.lc_part import *

class lc_thread:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_threads = {}

    def start(self, thread_path: str, thread_class: str):
        if not (thread_path in self.m_threads):
            module = getattr(import_module(thread_path), thread_class)
            self.m_threads[thread_path] = module(self.m_librecoin)
        if thread_path in self.m_threads:
            try:
                self.m_threads[thread_path].daemon=True
                self.m_threads[thread_path].start()
            except:
                self.m_threads[thread_path].stop()

    def stop(self):
        if thread_path in self.m_threads:
            self.m_threads[thread_path].stop()
