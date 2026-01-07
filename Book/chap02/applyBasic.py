import pandas as pd

filename = r'E:\KBK\python\Book\data\memberInfo.csv'

df = pd.read_csv(filename, index_col='id')

# plus 함수 선언
def plus(x) :
    return x + 5

print('\n# 시리즈와 apply 메소드')
print(df)

print('\n# 일반적인 산술 연산')
print(df['kor'] + 5)

print('\n# apply 함수를 적용한 결과')
print(df['kor'].apply(plus))

# gob 함수 선언
def gob(x, n) :
    return n * x

print('\n# gob(2) 결과, apply 로 곱셈 함수를 적용한 결과')
ex = df['kor'].apply(gob, n = 2)
print(ex)

print('\n# gob(3) 결과')
ex = df['kor'].apply(gob, n = 3)
print(ex)

# applyByColumn 함수 선언
def applyByColumn(col) :
    mysum = 0
    for item in col :
        mysum += item
    return mysum / df.shape[0]

print('\n# applyByColumn 결과')
print(df.apply(applyByColumn, axis = 0))

# applyByRow 함수 선언
def applyByRow(row) :
    mysum = 0
    for item in row :
        mysum += item
    return mysum / df.shape[1]

print('\n# applyByRow 결과')
print(df.apply(applyByRow, axis = 1))