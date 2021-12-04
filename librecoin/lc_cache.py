class cache:
    def __init__(self, p_md5_key: str):
        self.m_md5_key = p_md5_key

    ########################################################
    #
    def store(self, p_datas, p_file_name: str):
        # print("store_as_cache")

        try:
            if not path.exists('cache'):
                makedirs('cache')
            if not path.exists('cache/' + self.m_md5_key):
                makedirs('cache/' + self.m_md5_key)
            path_cache = 'cache/' + self.m_md5_key + '/' + file_name + '.cache'
            file_datas = open(path_cache, "w").write(datas)
            return True
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return False


    ########################################################
    #
    def exist(self, p_file_name: str):
        # print("cache_exist")

        path_cache = 'cache/' + self.m_md5_key + '/' + file_name + '.cache'
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
        if current_date > (modify_date + g_expire_time):
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
