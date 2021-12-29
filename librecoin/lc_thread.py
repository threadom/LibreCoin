from importlib import import_module

from librecoin.lc_part import *

class lc_thread:
    def __init__(self, librecoin: object):
        # print('lc_thread.init')
        self.m_librecoin = librecoin
        self.m_threads = {}

    def start(self, thread_path: str, thread_class: str):
        # print('lc_thread.start:'+thread_path+':'+thread_class)
        if not (thread_path in self.m_threads):
            module = getattr(import_module(thread_path), thread_class)
            self.m_threads[thread_path] = module(self.m_librecoin)
        if thread_path in self.m_threads:
            if not self.m_threads[thread_path].started():
                try:
                    self.m_threads[thread_path].daemon=True
                    self.m_threads[thread_path].start()
                except:
                    self.m_threads[thread_path].stop()

    def stop(self):
        # print('lc_thread.stop')
        if thread_path in self.m_threads:
            self.m_threads[thread_path].stop()
