import json

# import sqlite3
# from sqlite3 import Error

class lc_store:
    def __init__(self, librecoin: object):
        self.m_librecoin = librecoin
        self.m_database_type = self.m_librecoin.config().get("database_type")
        self.m_database_host = self.m_librecoin.config().get("database_host")
        self.m_database_base = self.m_librecoin.config().get("database_base")
        self.m_database_user = self.m_librecoin.config().get("database_user")
        self.m_database_pass = self.m_librecoin.config().get("database_pass")
        self.m_connection = False
        self.m_tableexist = {}

    def __connect(self):           
        # print("lc_store.__connect")
        if self.m_connection:
            return self.m_connection
        if self.m_database_type == "mariadb":
            import mariadb
            try:
                self.m_connection = mariadb.connect(
                    host=self.m_database_host,
                    database=self.m_database_base,
                    user=self.m_database_user,
                    password=self.m_database_pass
                )
                return self.m_connection
            except mariadb.Error as e: 
                print(f"Error connecting to MariaDB Platform: {e}") 
                sys.exit(1) 

        # /!\ Obsolete : sqlite3 don't support multi threading 
        # /!\ try:
        # /!\     db_file = "librecoin.db"
        # /!\     self.m_connection = sqlite3.connect(db_file)
        # /!\     return self.m_connection
        # /!\ except Error as e:
        # /!\     print(e)

    def __execute(self, query: str):
        if not self.m_connection:
            self.m_connection = self.__connect()
        if self.m_connection:
            cursor = self.m_connection.cursor()
            cursor.execute(query)
            self.m_connection.commit()


    def __query(self, query: str):
        if not self.m_connection:
            self.m_connection = self.__connect()
        if self.m_connection:
            cursor = self.m_connection.cursor()
            cursor.execute(query)
            
            return cursor.fetchall()

    
    def __tableexist(self, table: str):
        # print("lc_store.__tableexist")
        if table in self.m_tableexist:
            return True
        if self.m_database_type == "mariadb":
            query = "SHOW TABLES LIKE '" + table + "'";
            rows = self.__query(query)
            if len(rows) > 0:
                return True
        # if self.m_database_type == "sqlite":
        #     query = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + table + "'";
        #     rows = self.__query(query)
        #     if len(rows) > 0:
        #         return True

        return False

    def __createtable(self, table: str, datas_structure: str):
        # print("lc_store.__createtable")
        if self.__tableexist(table):
            return True
        if not self.m_connection:
            self.m_connection = self.__connect()
        if self.m_connection:
            query = "CREATE TABLE IF NOT EXISTS " + table + " ("
            query += "id integer PRIMARY KEY NOT NULL AUTO_INCREMENT,"
            query += "skey text,"
            for field in datas_structure:
                query += field + " " + datas_structure[field] + ","
            query = query[:-1]
            query += ");"
            self.__execute(query)
            self.m_tableexist[table] = True
            return True
        return False

    def store(self, table: str, skey: int, datas_structure: json, datas: json):
        # print("lc_store.store")
        if not self.m_connection:
            self.m_connection = self.__connect()
        if self.m_connection:
            if self.__createtable(table, datas_structure):
                query = "INSERT INTO " + table + " (skey,"
                for field in datas_structure:
                    query += field + ","
                query = query[:-1]
                query += ") VALUES ('" + skey + "',"
                for value in datas:
                    query += "'" + str(value) + "',"
                query = query[:-1]
                query += ");"
                self.__execute(query)
                return True
            return False
        return False

    def read(self, table: str, skey: int, filter_name: str, filter_min: int, filter_max: int):
        # print("lc_store.read")
        if not self.m_connection:
            self.m_connection = self.__connect()
        if self.m_connection:
            if self.__tableexist(table):
                query = "SELECT * FROM " + table
                query += " WHERE skey = '" + skey + "'"
                query += " AND " + filter_name + " >= " + str(filter_min)
                query += " AND " + filter_name + " <= " + str(filter_max)
                query += " ORDER BY " + filter_name + " DESC"
                return self.__query(query)
            return False
        return False
