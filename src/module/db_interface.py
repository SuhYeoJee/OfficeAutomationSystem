import sqlite3

class DBInterface:
    def __init__(self):
        self.db_name = 'nova.db'
        self.connection = None
        self.cursor = None
    # ===========================================================================================
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Connected to SQLite database '{self.db_name}'")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")
    # --------------------------
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from SQLite database '{self.db_name}'")
        else:
            print("Already disconnected from database")
        self.connection = None
        self.cursor = None
    # -------------------------------------------------------------------------------------------
    def ensure_connected(func):     # DB 연결 보장
        def wrapper(self, *args, **kwargs):
            if (self.connection is None) or (self.cursor is None):
                self.connect()
            try:
                return func(self, *args, **kwargs)
            finally:
                self.disconnect()  # 함수 호출 후 연결 종료
        return wrapper
    # ===========================================================================================
    @ensure_connected
    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            if query.strip().lower().split(' ')[0] in ['insert','delete','update']:
                self.connection.commit()
                return self.cursor.rowcount
            else:
                rows = self.cursor.fetchall()
                return rows
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return []
    # ===========================================================================================

if __name__ == "__main__":
    simple_db = DBInterface()
    query = "SELECT * FROM test;"
    rows = simple_db.execute_query(query)
    for row in rows: print(row)
