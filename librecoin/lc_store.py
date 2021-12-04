import json
import sqlite3
from sqlite3 import Error

class lc_store:
    m_connection = False

    @staticmethod
    def __connect():
        # print("lc_store.__connect")
        if lc_store.m_connection:
            return lc_store.m_connection
        try:
            db_file = "librecoin.db"
            lc_store.m_connection = sqlite3.connect(db_file)
            return lc_store.m_connection
        except Error as e:
            print(e)

    @staticmethod
    def __execute(query: str):
        # print("lc_store.__execute")
        conn = lc_store.__connect()
        if not conn: return False

        cursor = conn.cursor()
        # print(query)
        cursor.execute(query)
        conn.commit()


    @staticmethod
    def __query(query: str):
        # print("lc_store.__query")
        conn = lc_store.__connect()
        if not conn: return False

        cursor = conn.cursor()
        # print(query)
        cursor.execute(query)
        
        return cursor.fetchall()

    m_tableexist = {}
    @staticmethod
    def __tableexist(table: str):
        # print("lc_store.__tableexist")
        if table in lc_store.m_tableexist:
            return True
        return False

    @staticmethod
    def __createtable(table: str, datas_structure: str):
        # print("lc_store.__createtable")
        if lc_store.__tableexist(table):
            return True
        conn = lc_store.__connect()
        if not conn: return False

        # test if table exist
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + table + "'";
        rows = lc_store.__query(query)

        if not (len(rows) > 0):
            query = "CREATE TABLE IF NOT EXISTS " + table + " ("
            query += "id integer PRIMARY KEY,"
            query += "key text,"
            for field in datas_structure:
                query += field + " " + datas_structure[field] + ","
            query = query[:-1]
            query += ");"

            lc_store.__execute(query)

        lc_store.m_tableexist[table] = True
        return True

    @staticmethod
    def store(table: str, key: int, datas_structure: json, datas: json):
        # print("lc_store.store")
        conn = lc_store.__connect()
        if not conn: return False

        if lc_store.__createtable(table, datas_structure):
            query = "INSERT INTO " + table + " (key,"
            for field in datas_structure:
                query += field + ","
            query = query[:-1]
            query += ") VALUES ('" + key + "',"
            for value in datas:
                query += "'" + str(value) + "',"
            query = query[:-1]
            query += ");"
            lc_store.__execute(query)

        return False

    @staticmethod
    def read(table: str, key: int, filter_name: str, filter_min: int, filter_max: int):
        # print("lc_store.read")
        conn = lc_store.__connect()
        if not conn: return False

        if lc_store.__tableexist(table):
            query = "SELECT * FROM " + table
            query += " WHERE key = '" + key + "'"
            query += " AND " + filter_name + " >= " + str(filter_min)
            query += " AND " + filter_name + " <= " + str(filter_max)
            query += " ORDER BY " + filter_name + " DESC"
            return lc_store.__query(query)

        return False
