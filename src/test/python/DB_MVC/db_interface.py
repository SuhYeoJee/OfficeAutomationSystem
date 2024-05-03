import mysql.connector

class DBInterface:
    def __init__(self, username, password, database, port=3306, host='localhost'):
        self.config = {
            'user': username,
            'password': password,
            'host': host,
            'database': database,
            'port': port,
            'raise_on_warnings': True
        }
        self.connection = None
        self.cursor = None

    # [DB 연결] -------------------------------------------------------------------------------------------
    
    def connect(self):  # DB 연결
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            print("connect OK")
            return True
        except mysql.connector.Error as err:
            print(f"Error during connection: {err}")
            return False
        
    def disconnect(self):   # DB 연결 해제
        try:
            if self.is_connected():
                self.cursor.close()
                self.connection.close()
                print("disconnect OK")
        except mysql.connector.Error as err:
            print(f"Error during disconnection: {err}")
            return False
        else:
            return True
    
    def is_connected(self):     # DB 연결 확인
        if (self.connection is not None) and self.connection.is_connected():
            return True
        else:
            return False

    def ensure_connected(func):     # DB 연결 보장
        def wrapper(self, *args, **kwargs):
            if not self.is_connected():
                self.connect()
            try:
                return func(self, *args, **kwargs)
            finally:
                self.disconnect()  # 함수 호출 후 연결 종료
        return wrapper

    # [DB 동작] -------------------------------------------------------------------------------------------

    @ensure_connected
    def execute_query(self,query:str):  # DB 명령어 수행
        try:
            self.cursor.execute(query)
            if ('SELECT' in query) or ('DESCRIBE' in query):
                result = self.cursor.fetchall()
            else:
                self.connection.commit()
                result = True
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            result =  False
        finally:
            return result
    # -------------------------------------------------------------------------------------------


# ===========================================================================================
test_data = ["root","pass","nova","3307"]

def dbi_test():
    dbi = DBInterface(*test_data)
    res = dbi.execute_query("SELECT DISTINCT * FROM `powder` ; ")
    from pprint import pprint
    pprint(res)

if __name__ == "__main__":
    dbi_test()