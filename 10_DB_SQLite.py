# sqlite 버전 확인
import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)
print()


# 날짜 생성
import datetime

now = datetime.datetime.now()
print(now)

now2 = now.strftime('%Y-%m-%d %H:%M:%S') # 날짜/시간을 스트링으로 변환
print(now2)


# DB 생성 & Auto commit (Rollback)
# DB 생성
conn = sqlite3.connect('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/database.db', isolation_level = None) # Auto commit 을 위한 설정

# cursor
# 데이터를 읽어올 때 기준이 되는 커서
c = conn.cursor()

# 테이블 생성
# data type : text, numeric, integer, rear, blob
c.execute("CREATE TABLE IF NOT EXISTS users(id interger primary key, username text, email text, \
    phone text, website text, regdate text)")

