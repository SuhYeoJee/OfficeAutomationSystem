import sqlite3

# 데이터베이스에 연결 (파일 기반 데이터베이스)
conn = sqlite3.connect('nova.db')

# 커서 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# 데이터 삽입
cursor.execute('''
INSERT INTO test (name)
VALUES ('John Doe')
''')
cursor.execute('''
INSERT INTO test (name)
VALUES ('Jane Smith')
''')
cursor.execute('''
INSERT INTO test (name)
VALUES ('Mike Brown')
''')

# 커밋 (변경 사항 저장)
conn.commit()

# 데이터 조회
cursor.execute('SELECT * FROM test')
rows = cursor.fetchall()

# 조회된 데이터 출력
for row in rows:
    print(row)

# 연결 종료
conn.close()
