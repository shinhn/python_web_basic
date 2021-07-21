import csv

# csv 읽기
# ex1
with open('./resource/sample1.csv', 'r', encoding = 'euc-kr') as f: # 한글 encoding : utf-8 / utf-16 / euc-kr

    reader = csv.reader(f)
    print(dir(reader)) # dir로 출력해봤을 떄 '__iter__'이 있으면 반복문으로 출력해볼 수 있음
    print()

    # next(reader) -> 한 행을 스킵-> 보통 ['번호', '이름', '가입일시', '나이'] 같은 header을 스킵할 때 사용

    for c in reader:
        print(c)

print()

# ex2
with open('./resource/sample2.csv', 'r', encoding = 'euc-kr') as f:

    # reader = csv.reader(f)
    reader = csv.reader(f, delimiter='|') # sample2의 경우 '|'으로 구분되어 있기 때문에 구분선을 명시 해줘야 함
    print(dir(reader))
    print()

    for c in reader:
        print(c)

print()

# Dict 변환
with open('./resource/sample1.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c)

print()

with open('./resource/sample1.csv', 'r', encoding = 'euc-kr') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items(): # .items() : key와 value 값을 모두 가져옴
            print(k,v)
        print()





# csv 쓰기
# 한줄씩 쓰기 (정보를 하나씩 검수해서 처리할 때 용이)
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w') as f:
    wt = csv.writer(f)

    for value in w:
        wt.writerow(value)

# 한번에 쓰기 (검수, 처리할 필요 없이 전부 처리할 때 용이)
with open('./resource/sample4.csv','w') as f:
    wt = csv.writer(f)
    wt.writerows(w)




# Excel 읽기
# XSL, XLSX

import pandas as pd

f = pd.read_excel('./resource/sample.xlsx')
# 옵션
# ,sheetname = '시트명' or 숫자 : 가져올 excel 데이터의 sheetname 지정
# ,header = 숫자 : 몇번째 행을 header로 지정할껀지
# ,skiprow = 숫자 : 특정 행 스킵

print(f.head()) # 상위 5행 데이터 확인
print()

print(f.tail()) # 하위 5행 데이터 확인
print()

print(f.shape) # 행, 열 수 확인


# Excel 쓰기
f.to_excel('./resource/result.xlsx', index = False)