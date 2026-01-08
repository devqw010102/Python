# Q1
name = '김하늘'
birth_year = 2003
current_year = 2025

age = current_year - birth_year + 1
print('이름 : ' + name + ' 나이 : ' + str(age))
print('이름 : %s 나이 : %d' %(name, age))

# Q2
id_number = '990101-1234567'

print(id_number[:6:1])
print(id_number[7::])
# print(id_number[-7::])
print(id_number.replace('-', ''))
# String slice || [startIndex : endIndex : stepIndex]

# Q3
filename = 'report_final_v2.pdf'

print(filename[-3::])
print(filename[:-4:])

# Q4
text = 'abcabcabc'

print(text[::3])

# Q5
phone = '01011115222'

print(phone[:3:] + '-' + phone[3:7:] + '-' + phone[7::])

# Q6
a = '5'
b = 3

print(a * b) # 의 결과 : 555

# Q7
count = 7
print('총 개수 : ' + str(count) + '개')

# Q8
car_number = '12가3456'

print(len(car_number))
print(car_number[3::])

# Q9
print('★' * 10)

# Q10
name = '이준호'
score = 87

print('학생 %s의 점수는 %d점입니다.' %(name, score))
print('학생 ' + name + '의 점수는 ' + str(score) + '점입니다.')

# Q11
string = 'abcdfe2a354a32a'

print(string.replace('a', 'A'))

# Q12
t1 = 'python'
t2 = 'java'

print((t1 + ' ' + t2 + ' ') * 4)
print('%s %s ' %(t1, t2) * 4)

# Q13
bungi = '2020/03(E) (IFRS연결)'

print(bungi.split('(')[0])