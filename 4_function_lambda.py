# 함수
def hello(a):
    print("hello ", a)

hello("python")

# 리턴 함수
def hello_return(a):
    val = "hello " + str(a)
    return val

str = hello_return("python")
print(str)

# 다중 리턴 함수
def function(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

def function2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

val1, val2, val3 = function(2)
print(val1, val2, val3)

val4 = function2(2)
print(val4)

# 가변 매개 변수 함수 
# 1. *args (arguments): 여러 개의 인자를 함수로 받고자 할 때
# -> tuple 형태로 리턴

def args_function(*args):
    print(args)

args_function('kang')
args_function('kang', 'kim')
args_function('kang', 'kim', 'park')

# 2. **kwargs (keyword arguments): 딕셔너리 형태를 함수로 받고자 할 때
# -> 딕셔너리 형태로 리턴

def kawargs_function(**kwargs):
    print(kwargs)

kawargs_function(name1 = 'kang', name2 = 'kim', name3 = 'park')


# 혼합

def complex(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

complex(10, 20)
complex(10, 20, 'kang', 'kim')
complex(10, 20, 'kang', 'kim', arg3 = 1, arg4 = 2)


# hint
# 입출력 결과 자체는 동일
# 함수의 입력과 출력값의 형태를 한눈에 보기 좋게 명시하는 방법
def function2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

def function2(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


# lambda
# : 메모리 절약, 가독성 향상, 코드 간결 but 너무 lambda를 남발하면 오히려 가독성이 떨어짐
# 함수 - 객체 생성 -> 리소스(메모리) 할당
# 람다 - 즉시 실행 (Heap 초기화) -> 메모리 초기화

# 함수 - 변수 할당
def fuction_mul(num : int) -> int:
    return num * 10

print(fuction_mul(10))

# 람다
lambda_mul = lambda num : num * 10

print(lambda_mul(10))


# 함수 매개변수
# 함수를 매개변수로 이용할 수도 있음
def fuction_fuction(x, y, func):
    print(x * y * func(10))

fuction_fuction(2, 4, lambda_mul)