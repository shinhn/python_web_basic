import random
import time
import pygame # 소리 재생을 위한 패키지
import datetime
import sqlite3

# 소리 설정
pygame.init() # 꼭 초기화를 해주고 사용해야 함
correct_sound = pygame.mixer.Sound('/Users/kangshinhyeon/Documents/github/python_web_basic/sound/good.wav')
wrong_sound = pygame.mixer.Sound('/Users/kangshinhyeon/Documents/github/python_web_basic/sound/bad.wav')

# db 제작
# db 생성 & auto commit
conn = sqlite3.connect('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/typing_game.db', isolation_level=None)

# cursor 연결
cursor = conn.cursor()

# table 생성
cursor.execute("CREATE TABLE IF NOT EXISTS records \
    (id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)") 

# AUTOINCREMENT : insert를 굳이 해주지 않아도 자동으로 증가




# 기능 구현

words = []

n = 1 # 게임 시도 횟수
cor_cnt = 0 # 정답 개수

with open('/Users/kangshinhyeon/Documents/github/python_web_basic/resource/word.txt','r') as f:
    for c in f:
        words.append(c.strip()) # .strip() : 단어의 양쪽 공백 제거

# 단어 리스트 확인
print(words)

input("Press Enter Key !") # 입력 (아무거나 상관없음, 안해도 무방) 후 엔터를 쳐야 다음으로 넘어감 (프로그램 실행)

# 시작 시간 측정
start = time.time()

while n<=5:
    random.shuffle(words) # 단어들을 무작위로 섞어줌
    q = random.choice(words) # 단어들 중 무작위로 하나 선택

    print()

    print("Question # {}".format(n))
    print(q) # 문제 출력

    x = input() # 정답 입력

    print()

    if str(q).strip() == str(x).strip(): # 문제(공백제거한)와 정답(공백제거한)이 일치할 경우
        print("Correct!")
        cor_cnt += 1
        correct_sound.play()
    else:
        print("Wrong!")
        wrong_sound.play()

    n += 1

end = time.time() # 종료 시간 측정
entire = end - start # 게임 시간 계산
entire = format(entire, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# db 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') \
    VALUES (?, ?, ?)", (cor_cnt, entire, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


# 게임 시간, 정답 개수 출력
print("게임 시간 : ", entire, "초", "정답 개수 : {}".format(cor_cnt))



