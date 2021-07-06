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

# ----------------------------------------------------------------------------------------
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

# 삭제 (index 기준)
del c[1]
print(c)
del c[-1]
print(c)

# 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)

# sort : 정렬
y.sort()
print(y)

# reverse
y.reverse()
print(y)

# insert
y.insert(2, 7) # 2번 index에 7삽입
print(y)

# 삭제 함수 (원소값 기준)
y.remove(2)
print(y)

# pop : 마지막 원소를 꺼냄 (LIFO)
y.pop()
print(y)

# extend : 끝에 연장
tmp = [88,77]
y.extend(tmp)
print(y)

y.append(tmp) # extend는 리스트 내 원소가 들어가고 append는 리스트 자체가 들어감
print(y)

# ----------------------------------------------------------------------------------------
# 튜플 : 순서 있음, 중복 허용, 수정 & 삭제 불가능
# 중요한 계좌번호, 개인정보 등 수정될 경우 오류를 일으키는 경우에 사용

a = ()
b = (1,)
c = (1, 2, 3, 4)

# del c[2] -> TypeError: 'tuple' object doesn't support item deletion

d = (10, 100, ('a','b','c'))

print()

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)

print()

# 함수
z = (5, 2, 1, 3, 4, 2)

print(z)
print(3 in z)
print(z.index(1))
print(z.count(2))

# ----------------------------------------------------------------------------------------
# 딕셔너리 (Dictionary)
# : 순서X, 중복X, 수정O, 삭제O

a = {'name':'Kang', 'phone':'010-0000-0000', 'birth': 980823}
b = {0:'hello', 1:'bye'}
c = {'arr':[1, 2, 3, 4, 5]}


# 출력
# 1.직접접근
print(a['name'])
# 없는 key로 접근할 경우 error

# 2.get
print(a.get('name'))
# 없는 key로 접근할 경우 None 출력

print(c['arr'][1:3])
print()

# 추가
a['address'] = 'Seoul'
print(a)

a['rank_list'] = [1,2,3]
a['rank_tuple'] = (1,2,3)
print(a)
print()

# keys
print(a.keys())
print(list(a.keys()))
print()

# values
print(a.values())
print(list(a.values()))
print()

# items
print(a.items())
print(list(a.items())) # list안의 tuple 형태로 출력
print()


# ----------------------------------------------------------------------------------------
# 집합 (Sets)
# : 순서X, 중복X

a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(c) # 중복을 허용하지 않기 때문에 6은 한번만 출력
print()

# 집합은 보통 형 변환을 사용하여 인덱싱, 슬라이싱을 함
print(b)

t = tuple(b)
print(t)

l = list(b)
print(l)
print()


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
# 1. intersection
print(s1.intersection(s2))
# 2. &
print(s1 & s2)
print()

# 합집합 
# (집합 자체가 중복을 허용하지 않기 때문에 같은 부분은 한번만 포함됨)
# 1. union
print(s1.union(s2))
# 2. |
print(s1 | s2)
print()

# 차집합
# 1. difference
print(s1.difference(s2))
# 2. -
print(s1 - s2)
print()


# 추가, 제거
s3 = set([7, 8, 10, 15])
print(s3)
s3.add(18)
print(s3)
s3.remove(10)
print(s3)