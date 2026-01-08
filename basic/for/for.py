# 반복문 (for)

# 1. for in range()
for i in range(0, 10, 1):   # for(int i = 0; i < 10; i++) equal from Java
    print(i, end= ' ')

print('\n========================')

for i in range(0, 10) :     # 증감식 생략(Default = 1)
    print(i, end = ' ')

print('\n========================')

for i in range(10) :        # Start Index 생략(Default = 0)
    print(i, end= ' ')

print('\n========================')

# 2. for in instance
for i in 'abc' :
    print(i, end = ' ')

print('\n========================')

for i in [1, 2, 3] :
    print(i, end = ' ')

print('\n========================')

for i in [1, 2, 3] :
    if i % 2 == 0 :
        print(i, end = ' ')

print('\n========================')

numList = []
for i in range(3) :
    numList = int(input('홀/짝 구분할 숫자를 입력하세요.'))
    print('짝' if numList % 2 == 0 else '홀')
