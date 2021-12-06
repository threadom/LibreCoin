import time
import hashlib
from os import path
from os import makedirs
import datetime

class lc_cache:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_cache_key = ""
        self.m_cache_key = self.cache_key()

    ########################################################
    # Init md5 key for cache
    def cache_key(self):
        # print("cache_key")

        # read from globals if exist
        if self.m_cache_key:
            return self.m_cache_key

        # do it if nothing else exist
        coinbase_api_key = ""
        coinbase_api_secret = ""
        if "coinbase_api_key" in self.m_librecoin.m_json_config:
            coinbase_api_key = self.m_librecoin.m_json_config['coinbase_api_key'];
        if "coinbase_api_secret" in self.m_librecoin.m_json_config:
            coinbase_api_secret = self.m_librecoin.m_json_config['coinbase_api_secret'];

        # init globals before return
        self.m_cache_key = hashlib.md5((coinbase_api_key + "|" + coinbase_api_secret).encode()).hexdigest();

        if not self.m_cache_key:
            print("error: unable to generate cash key !")
            return False
        return self.m_cache_key

    ########################################################
    #
    def store(self, p_datas, p_file_name: str):
        # print("store_as_cache")
        if not self.cache_key():
            return False

        try:
            if not path.exists('cache'):
                makedirs('cache')
            if not path.exists('cache/' + self.m_cache_key):
                makedirs('cache/' + self.m_cache_key)
            path_cache = 'cache/' + self.m_cache_key + '/' + p_file_name + '.cache'
            file_datas = open(path_cache, "w").write(p_datas)
            return True
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return False


    ########################################################
    #
    def exist(self, p_file_name: str):
        # print("cache_exist")
        if not self.cache_key():
            return False

        path_cache = 'cache/' + self.m_cache_key + '/' + p_file_name + '.cache'
        if path.exists(path_cache):
            if self.is_expired(path_cache):
                return False
            return path_cache
        return False


    ########################################################
    #
    def is_expired(self, p_path_cache: str):
        # print("cache_is_expired")

        # get file modify date
        modify_date = time.ctime(path.getmtime(p_path_cache))
        modify_date = datetime.datetime.strptime(modify_date, "%a %b %d %H:%M:%S %Y")
        modify_date = modify_date.timestamp()

        # get current date
        current_date = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        current_date = current_date.timestamp()

        # if expired return True else False
        cache_expire_time = 300
        if "cache_expire_time" in self.m_librecoin.m_json_config:
            cache_expire_time = self.m_librecoin.m_json_config['cache_expire_time'];
        if current_date > (modify_date + cache_expire_time):
            return True
        return False


    ########################################################
    #
    def read(self, p_file_name: str):
        # print("read_from_cache")

        path_cache = self.exist(p_file_name)
        if path_cache:
            file_datas = open(path_cache, "r").read()
            return file_datas
        return ""


