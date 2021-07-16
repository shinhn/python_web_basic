# 읽기 모드 : r
# 쓰기 모드 (기존 파일 삭제) : w
# 추가 모드 (파일 생성 or 추가) : a
# .. : 상대경로 / . : 절대경로

# 파일 읽기
# 1. open(), 'r', read()
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
f.close() # 반드시 사용이 끝난 resource는 close로 닫아줘야함
print()


# 2. with
# open 만 사용했을 경우와 다르게 끝에 close()로 닫아주지 않아도 됨
with open('./resource/review.txt', 'r') as f :
    c = f.read()
    print(c)
print()


# 3. 한줄씩 출력
with open('./resource/review.txt', 'r') as f :
    for c in f:
        # print(c)
        print("->",c.strip()) # : 양쪽 공백 제거
print()


# 4. 커서 이동
with open('./resource/review.txt', 'r') as f :
    c = f.read()
    print("->", c)
    c = f.read() # 이미 한번 읽었기 때문에 커서가 맨끝에 위치하므로 읽을 내용이 없음
    print("->", c)
print()
print()


# 5. readline() : 한줄 읽음
with open('./resource/review.txt', 'r') as f :
    line = f.readline()
    while line:
        print(line, end = '->')
        line = f.readline()
print()
print()


# 6. readlines() : list 형태로 한줄씩 읽어 가지고 있음
with open('./resource/review.txt', 'r') as f :
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end = '->')
print()
print()


# 7. 내용 읽어온 뒤 계산
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score))) # {:6.3} - 문자열 포매팅 :  6자리이면서 소숫점 3자리까지 형식 선언
print()


# 파일 쓰기
# 1. open(). 'w', write()
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman!')

# 2. 내용 추가 'a'
with open('./resource/text1.txt', 'a') as f:
    f.write('\n-> Kang')

# 3. random
from random import randint # 정수를 random하게 반환

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50))) # 1 ~ 50
        f.write('\n')


# 4. writelines : 리스트를 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kang\n', 'Kim\n', 'Park\n']
    f.writelines(list)

# 5. print으로 파일 쓰기
with open('./resource/text4.txt', 'w') as f:
    print("print content1", file=f)
    print("print content2", file=f)