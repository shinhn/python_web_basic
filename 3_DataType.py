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
v_int = 7
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

i1 = 39
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