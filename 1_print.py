# print 구문의 이해

# 기본출력
print('Hello world!')
print("Hello world!")
print("""Hello world!""")
print('''Hello world!''')

print() # 아무것도 출력하지 않음 -> enter효과

# separator
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('rkdrpgml','naver.com',sep='@')

# end
print('Welcom To', end=' ')
print('the black parade', end=' ')
print('piano notes')
print()

# format [], {}, ()
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('Eunki', 7))

print("Test1 : %5d, price : %4.2f" % (776, 6534.123))
print("Test1 : {0: 5d}, price :{1: 4.2f}".format(776, 6543.123))
print("Test1 : {a: 5d}, price :{b: 4.2f}".format(a=776, b=6543.123))
print()

# Escape 코드
"""
\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
"""

print("'you'")
print('"you"')

print('\'you\'') # \다음 문자는 문자 그대로 출력
print('\\you\\') 

print('\\you\\\n\n') # \n = enter
print('\t\tyou') # \t = 들여쓰기

