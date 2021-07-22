# db 수정, 삭제

# db 연결
import sqlite3
conn = sqlite3.connect('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/database.db')

# cursor 연결
c = conn.cursor()



# # UPDATE

# # - tuple
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('man1', 2))
# conn.commit() # commit을 해줘야 db에 반영됨

# # - dictionary
# c.execute("UPDATE users SET username = :NAME WHERE id = :ID", {'NAME' : 'man2', 'ID' : 3})
# conn.commit()

# # - string
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('man3', 4))
# conn.commit()


# # data 중간 확인
# for user in c.execute("SELECT * FROM users"):
#     print(user)



# # DELETE
# # - tuple
# c.execute("DELETE FROM users WHERE id = ?", (2,))
# conn.commit()

# # - dictionary
# c.execute("DELETE FROM users WHERE id = :ID", {'ID' : 5})
# conn.commit()

# # - string
# c.execute("DELETE FROM users WHERE id = '%s'" % 4)
# conn.commit()

# # data 중간 확인
# for user in c.execute("SELECT * FROM users"):
#     print(user)

# # 전체 삭제
# print("count deleted row : ", conn.execute("DELETE FROM users").rowcount)
# conn.commit()


# 접속 해제
conn.close()
