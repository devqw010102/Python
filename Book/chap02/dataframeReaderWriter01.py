import numpy as np  # 수치 계산용 lib
import pandas as pd  # 데이터 분석용 lib
from tabulate import tabulate

myIndex = ['이순신' ,'김유신', '강감찬', '광해군', '연산군']
myColumns = ['서울', '부산', '광주', '목포', '경주']
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)

myframe = pd.DataFrame(np.reshape(mylist, (5, 5)), index = myIndex, columns = myColumns)
print(tabulate(myframe, tablefmt="fancy_grid"))

print('\n# 1행만 Series로 읽어 오기')
result = myframe.iloc[1]
print(type(result))
print(result)

# print('\n# result2')
# result2 = myframe.iloc[[1]]
# print(result2)
# print('\n# result3')
# result3 = myframe.iloc[[1, 3]]
# print(result3)

print('\n# 짝수행만 가져 오기')
result = myframe.iloc[0 : : 2]
print(result)

print('\n# 홀수행만 가져오기')
print('\n# 이순신 행만 Series로 읽어 오기')
result = myframe.loc['이순신']
print(type(result))
print(result)

print('\n# 이순신 행만 DataFrame으로 읽어 오기')
result = myframe.loc[['이순신']]
print(type(result))
print(result)

print('\n# 강감찬과 이순신 행 읽어 오기')
result = myframe.loc[['이순신', '강감찬']]
print(type(result))
print(result)

# print('-' * 40)
# print(myframe.index)
print('-' * 40)
myTarget = np.random.choice(myframe.index, 3)
print(myTarget)
print('-' * 40)
myTarget = np.random

# dataframe.loc[[행목록],[열목록]]
print('\n# 강감찬의 광주 실적 정보 가져 오기')
result = myframe.loc[['강감찬'], ['광주']]   # DataFrame
print(result)

print('\n# 연산군과 광해군의 광주/목포 정보 가져 오기')
result = myframe.loc[['연산군', '강감찬'], ['광주', '목포']]
print(result)

print('\n# 연속적인 데이터 가져 오기')
result = myframe.loc['김유신' : '광해군', '광주' : '목포']
print(result)

print('\n# 김유신 ~ 광해군까지 부산 실적 정보 가져 오기')
result = myframe.loc['김유신' : '광해군', ['부산']]
print(result)

print('\n# Boolean으로 데이터 처리하기')
result = myframe.loc[[False, True, True, False, True]]
print(result)

print('\n# 부산 실적이 100이하인 항목들')
result = myframe.loc[myframe['부산'] <= 100]
print(result)

print('\n# 목포 실적이 140인 항목들')
result = myframe.loc[myframe['목포'] == 140]
print(result)

# 부산 실적이 70 이상, 목포 실적이 140 이상인 항목 구하여 all(), any() 적용
cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140

print('-' * 40)

print(cond1)
print('-' * 40)
print(cond2)

df = pd.DataFrame([cond1, cond2])
print('\n# df 출력')
print(df)
print('\n# df.all() 출력')
print(df.all())

print('\n# df.all() Result 출력')
result = myframe.loc[df.all()]
print(result)

print('\n# df.any() Result 출력')
result = myframe.loc[df.any()]
print(result)

print('\n# 람다 함수의 사용')
result = myframe.loc[lambda df : df['광주'] >= 130]
print(result)

print('\n# 이순신과 강감찬의 부산 실적을 30으로 변경하기')
myframe.loc[['이순신', '강감찬'], ['부산']] = 30
print(tabulate(myframe, tablefmt="fancy_grid"))

print('\n# 김유신부터 광해군까지 경주 실적을 80으로 변경')
myframe.loc['김유신' : '광해군', ['경주']] = 80
print(myframe)

print('\n# 연산군의 모든 실적을 50으로 변경하기')
myframe.loc[['연산군'], :] = 50
print(myframe)

print('\n# 모든사람의 광주 컬럼을 60으로 변경')
myframe.loc[:, ['광주']] = 60
print(myframe)

print('\n# 경주 실적이 150이하인 데이터중 경주, 광주를 0으로 변경')
myframe.loc[myframe['경주'] <= 150, ['경주', '광주']] = 0
print(myframe)

print('\n# 데이터 프레임 사용')
print(myframe)