# 2. db 조회, 순회, dump(파일로 저장)

import sqlite3

# db파일 연결
# 없으면 새로 생성
conn = sqlite3.connect('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/database.db')

# 커서 바인딩
c = conn.cursor()




# # 조회
# # 커서를 전체
# c.execute("SELECT * FROM users") # 본 작업으로 커서를 위치시켜야 위에서 부터 한줄씩 조회가 가능함

# # 커서 위치에 따라 데이터 조회
# # - 1개 로우
# print('one : \n', c.fetchone())
# print()

# # - 3개 로우
# print('tree : \n', c.fetchmany(size = 3))
# print()

# # - 전체 로우
# print('all : \n', c.fetchall())
# print()
# print('all : \n', c.fetchall())
# print()




# Retrieve (순회)
# - c.execute 이후 c.fetchall 하는 방법
# c.execute("SELECT * FROM users") # 본 작업으로 커서를 위치시켜야 위에서 부터 한줄씩 조회가 가능함

# for r in c.fetchall():
#     print('-> ', r)

# - 쿼리문에 다 넣는 방법
# 쿼리문이 길어지기 때문에 코드의 가독성이 떨어진다는 단점
for r in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('-> ', r)

print()




# WHERE

# 한개 조회
# - tuple로 binding
param1 = (3,)
c.execute("SELECT * FROM users WHERE id = ?", param1)
print('param1', c.fetchone())
print()

# - interger로 binding
param2 = 4
c.execute("SELECT * FROM users WHERE id = '%d'" % param2)
print('param2', c.fetchone())
print()

# - dictionary로 binding
c.execute("SELECT * FROM users WHERE id = :ID", {"ID" : 5})
print('param3', c.fetchone())
print()


# 여러개 조회
# - tuple로 binding
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)
print('param4', c.fetchall())
print()

# - interger로 binding
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,5))
print('param5', c.fetchall())
print()

# - dictionary로 binding
c.execute("SELECT * FROM users WHERE id = :ID1 OR id = :ID2", {'ID1' : 2, 'ID2' : 4})
print('param6', c.fetchall())
print()




# Dump
# database를 file로 저장하여 백업하는 기능
with conn:
    with open('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/dump.sql', 'w') as f: 
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('complet Dump!')

 # with conn -> conn.close()가 내장되어 있기 때문에 뒤에서 따로 처리하지 않아도 됨
# with open() as f -> f.close()가 내장되어 있기 때문에 뒤에서 따로 처리하지 않아도 됨