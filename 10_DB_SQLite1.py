# 1. db 생성, 삽입

# sqlite 버전 확인
import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)
print()


# 날짜 생성
import datetime

now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') # 날짜/시간을 스트링으로 변환
print(nowDatetime)



# DB 생성 & Auto commit (Rollback)
# DB 생성
conn = sqlite3.connect('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/database.db', isolation_level = None) # Auto commit 을 위한 설정



# cursor
# 데이터를 읽거나 쓸 때 기준이 되는 커서
# 삽입한 마지막 위치에 이어서 data를 삽입할 예정이므로 삽입 할 때마다 conn.corsor()하기 번거로우므로 c에 받아 놓음
c = conn.cursor()



# 테이블 생성
# data type : text, numeric, integer, rear, blob
# c.execute("CREATE TABLE IF NOT EXISTS TableName(DataName1 Type, DataName2 Type, DataName3 Type, ...)")

c.execute("CREATE TABLE IF NOT EXISTS users(id interger primary key, username text, email text, \
    phone text, website text, regdate text)")



# data 삽입


# 1. VALUES에 순서대로 일괄적으로 삽입
# c.execute("INSERT INTO users \
# VALUES(Data1, Data2, Data3, ...)")

# c.execute("INSERT INTO users \
# VALUES(1, 'Kang', 'rkdrpgml@naver.com', '010-0000-0000', 'shinhn.github.io', ?)", (nowDatetime,)) # ? 는 뒤에 순서대로 매칭됨



# 2. 삽입할 DataName을 지정 후 삽입
# c.execute("INSERT INTO users(DataName1, DataName2, DataName3, ...) \
# VALUES(Data1, Data2, Data3, ...)")

# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) \
#     VALUES(?,?,?,?,?,?)", (2, 'park', 'park@naver.com', '010-1111-1111', 'park.github.io', nowDatetime))

# cf) id(primary key)에 같은 값을 또 넣어주면 error가 발생함



# 3. Many 삽입 - 튜플안의 튜플들
# c.executemany("INSERT INTO users(DataName1, DataName2, DataName3, ...) \
# VALUES(Data1, Data2, Data3, ...)", tuples)

userList = (
    (3, 'Lee', 'Lee@naver.com', '010-3333-3333', 'Lee.github.io', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-4444-4444', 'Cho.github.io', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-5555-5555', 'Yoo.github.io', nowDatetime)
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
#     VALUES (?,?,?,?,?,?)", userList)




# data 삭제
# - 일괄 삭제
# conn.execute("DELETE FROM users")

# - 일괄 삭제 후 삭제된 row 수 반환
# conn.execute("DELETE FROM TableName").rowcount
# print("count deleted row : ", conn.execute("DELETE FROM users").rowcount)



# commit 
# - Auto commit : database 생성시 ", isolation_level = None" 옵션을 넣어주면 됨
# - Non Auto commit : 위와 같은 옵션을 설정해주지 않으면 conn.commit() 명령어로 매번 commit 해야 함



# rollback
# conn.rollback()



# 접속 해제
# conn.close()

