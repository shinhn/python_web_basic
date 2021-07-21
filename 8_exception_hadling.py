# 예외 종류
# linter : 코드 스타일, 문법 체크
# syntaxError : 잘못된 문법
# ZeroDivisionError : 0 나누기 에러
# IndexError : 인덱스 범위 오버
# keyError : 주로 딕셔너리에서 발생
# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# ValuError : 참조 값이 없을 때 발생
# FileNotFoundError : 파일이 현재 경로에 없을 때 발생
# TypeError

# 예외 처리
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# list에 있는 경우
try:
    z = 'Lee'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occured Error!')
else:
    print('예외 없을 경우')
finally:
    print('무조건 실행')

print()

# list에 없는 경우
try:
    z = 'Kang'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except:
    print('Not found it! - Occured Error!')
else:
    print('예외 없을 경우')
finally:
    print('무조건 실행')

print()

# 예외 처리는 하지 않지만, 무조건 수행하는 코딩 패턴
try:
    print('작업')
finally:
    print('작업 후 무조건 실행')

# 다양한 예외 처리
# except 문이 순차적으로 수행되기 때문에 전체 예외를 처리하는 Exception을 마지막에 둬야 함
try:
    z = 'Lee'
    x = name.index(z)
    print('{} found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
except IndexError:
    print('Not found it! - Occured IndexError!')
except Exception:
    print('Not found it! - Occured EveryError!')
else:
    print('예외 없을 경우')
finally:
    print('무조건 실행')

print()

# 예외 발생
# raise
# 일부러 예외를 발생시켜 특정 상황에 관리자가 로그 기록을 알아야 하는 경우 등에 활용 가능
try:
    a = 'Kim'
    if a == 'Kim':
        print('ok!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
else:
    print('ok!')