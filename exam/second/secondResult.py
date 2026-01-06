# Q1
q1 = [3, -20, -3, 44]

for i in q1 :
    if i < 0 :
        print(i)

# Q2
q2 = [3, 100, 23, 44]

for i in q2 :
    if i % 3 == 0 :
        print(i)

# Q3
q3 = [13, 21, 12, 14, 30, 18]

for i in q3 :
    if i < 20 and i % 3 == 0 :
        print(i)

# Q4
q4 = ["I", "study", "python", "language", "!"]

for i in q4 :
    if len(i) >= 3 :
        print(i)

# Q5
q5 = ['hello.py', 'ex01.py', 'intro.hwp']

for i in q5 :
    print(i.split('.')[0])

# Q6
q6 = input('휴대전화 번호 입력: ')
num = q6.split('-')[0]

telecom_map = {
    '011': 'SKT',
    '016': 'KT',
    '019': 'LGU',
    '010': '알수없음'
}

print(f"당신은 {telecom_map.get(num)} 사용자 입니다.")

# Q7
q7 = input('우편번호: ')
q = q7[2:3:]

if q in '012':
    print('강북구')
elif q in '345':
    print('도봉구')
elif q in '6789':
    print('노원구')