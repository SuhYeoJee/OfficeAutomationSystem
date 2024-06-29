if __debug__:
    import sys
    sys.path.append(r"D:\Github\OfficeAutomationSystem")
import sqlite3

def get_triggers_for_table(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # 특정 테이블의 트리거 정보 조회
        cursor.execute(f"SELECT name, tbl_name, sql FROM sqlite_master WHERE type='trigger' AND tbl_name='{table_name}';")
        triggers = cursor.fetchall()

        for trigger in triggers:
            print(f"Trigger Name: {trigger[0]}")
            print(f"Table Name: {trigger[1]}")
            print(f"SQL Definition:\n{trigger[2]}\n")

        return triggers

    except sqlite3.Error as e:
        print(f"Error retrieving triggers: {e}")
        return []

    finally:
        conn.close()

# 사용 예시
db_file = 'src/data/nova.db'
table_name = 'customer'
triggers = get_triggers_for_table(db_file, table_name)
print(triggers)
