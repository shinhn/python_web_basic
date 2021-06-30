# python data type 종류
  
# Boolean - 참(1), 거짓(0)
# Numbers - 정수, 실수
# String
# Bytes
# Lists
# Tuples
# Sets
# Dictionaries

# 집합 자료형 : Lists / Tuples / Sets / Dictionaries

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 8
v_dict = {
    "name" : "kim", # key_value
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1)) # 어떤 data type인지 출력
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

# python 숫자형 및 연산자

# + (더하기)
# - (빼기)
# * (곱하기)
# / (나누기)
# // (나누기-몫)
# % (나누기-나머지)
# ** (지수 제곱)
# 단항 연산자

i1 = 38
i2 = 939
big_int1 = 9999999999999999999999999999
big_int2 = 7777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)

print(f3 + i2) # 정수 + 실수 => 실수가 껴있으면 실수로 출력
result = f3 + i2
print(result, type(result))

a = 5.
b = 4
print(type(a), type(b))

result2 = a+b
print(result2)

# 형변환
# int, float, complex(복소수)
print(int(3.0))
print(float(3))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

# 수치 연산 함수
print(abs(-7)) # 절댓값
n, m = 30, 20
n, m = divmod(100,8) # 100을 8로 나눈 몫을 n에, 나머지를 m에 대입함
print(n,m)

import math
print(math.ceil(5.1)) # 5.1보다 큰 정수중 가장 작은 정수
print(math.floor(3.874)) # 3.874보다 작은 정수중 가장 큰 정수


# 문자열

str1 = "I am \"shinhyeonKang.\"" # 문자 그대로 출력할때 \(escape) 이용
str2 = 'Man'
str3 = ''
str4 = ' '
str5 = 'Tab\tTab\tTab' # \t 은 tap(= 공백4칸)을 해줌

print(str1, len(str1))
print(str2, len(str2))
print(str3, len(str3))
print(str4, len(str4))
print(str5, len(str5))


# Raw String

raw_s1 = r'/Users/kangshinhyeon/documents/github/python_web_basic/bin'
print(raw_s1)


# 멀티라인
# '\'을 통해 enter한 다음부터 내용임을 알려줌 (안해주고 enter바로 하면 오류)
multi_line = \
"""
내용

그대로

출력
"""
print(multi_line)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'

print(str_o1 * 100)
print(str_o2 + str_o3)

# in / not in 문자열안에 문자 혹은 문자열이 존재하는지 확인
print('e' in str_o3)
print('a' in str_o3)
print('a' not in str_o3)

# 문자열 형 변환
print(str(77) + 'a')

# 문자열 함수
a = 'shinhyeon'
print(a.capitalize()) # 첫번째 문자를 대문자로 변환
print(a.replace('on', 'ON'))

# 문자열 슬라이싱
a = 'shinhyeon'
print(a[0:3])
print(a[0:4:2]) # 4까지 2개씩
print(a[1:-2])
print(a[::-1]) # -1부터 전부

# 리스트

# 리스트 : 순서 있음, 중복 허용, 수정 & 삭제 가능
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'apple', 'banana']
e = [10, 100, ['apple', 'banana','orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(e[2][1]) # 2번 index 요소의 1번 index 요소 출력

# 슬라이싱
print(d[0:3])
print(e[2][0:2])

# 연산
print(c+d)
print(c*3)
print(str(c[0]) + 'list')

# 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a','b','c']
print(c)

# 삭제
del c[1]
print(c)
del c[-1]
print(c)

# 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2, 7) # 2번 index에 7삽입
print(y)
