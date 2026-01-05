word = 'python'
print(word)
print(word[0], word[2])

license_number = '24가 3465'
# 문자열 슬라이싱([시작인덱스 : 끝인덱스 : 단계])
# 시작인덱스 생략 : 0, 끝인덱스 생략 : 문자열 끝까지
# 아래 3개는 같은 결과
print(license_number[4:8:1])
print(license_number[4::1])
print(license_number[-4:])
# 인덱스가 음수면 뒤에서 부터
print(license_number[-1:-5:-1]) # reverse

string = '홀짝홀짝홀짝'
print(string[::2])

phone_number = '010-1111-2222'

# 전화번호에서 하이픈 제거
print(phone_number.replace('-', ''))

# 문자열 합치기
a = '3'
b = '4'
print(a + b)

# 문자열 * 숫자 : 문자열을 숫자만큼 반복
print('hi' * 3)

# 출력 형식
# 파이썬에서 문자 + 숫자 허용 X
name1 = '김민수'
name2 = '이철희'
age1 = 10
age2 = 20

# 아래 2개는 같은 형식으로 출력
print('이름 : ' + name1 + ', 나이 : ' + str(age1))
print('이름 : %s, 나이 : %d' % (name2, age2))

# split(문자열 나누기)
s = 'hello world'
print(s)
print(s.split(' '))

data = '2020-05-01'
print(data)
print(data.split('-'))