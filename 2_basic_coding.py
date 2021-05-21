# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이썬의 철학 및 장점들 출력됨

# python3의 입력 및 출력 기본 인코딩
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)
# utf_8임을 알 수 있음

# 출력문
print('My name is shinhyeon.')

# 변수 선언
name = 'shinhyeon'

# 조건문
if name == 'shinhyeon':
    print('correct')

# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

# 함수선언
def A():
    print('안녕')

A()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
