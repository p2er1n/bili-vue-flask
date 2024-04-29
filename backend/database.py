import time
import sqlite3

_db_file_name = "sqlite.db"

def _table_exists(table, cur):
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,))
    res = cur.fetchone()
    if res == None:
        return False
    else:
        return True

def _create_table(table, cur):
    sql_command = f"CREATE TABLE {table} (title TEXT, view INTEGER, danmaku INTEGER, favorite INTEGER, coin INTEGER, share INTEGER, author_name TEXT, author_face TEXT, category TEXT, rank INTEGER PRIMARY KEY, time INTEGER);"
    cur.execute(sql_command)

def _check_and_drop_table(table, cur):
    if not _table_exists(table, cur):
        return
    res = cur.execute(f"SELECT time FROM {table}").fetchone()
    if res != None:
        ct = int(time.time())
        if abs(ct - res[0]) >= (5 * 3600):
            print(f"{table} is outdated")
            cur.execute(f"DROP TABLE {table};")


def store(value, table):
    with sqlite3.connect(_db_file_name) as conn:
        try:
            cur = conn.cursor()
            if not _table_exists(table, cur):
                _create_table(table, cur)
            cur.execute(f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", value)
            conn.commit()
        finally:
            cur.close()
            
def get(category, table=None, default=None):
    if table == None:
        table = category    
    with sqlite3.connect(_db_file_name) as conn:
        try:
            cur = conn.cursor()
            _check_and_drop_table(table, cur)
            if not _table_exists(table, cur):
                _create_table(table, cur)
            res = cur.execute(f"SELECT * FROM {table} WHERE category=? ORDER BY rank", (category,)).fetchall()
            if len(res) <= 0:
                return default
            return res
        finally:
            cur.close()
        
