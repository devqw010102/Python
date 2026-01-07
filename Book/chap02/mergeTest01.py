import pandas as pd

dict1 = {'name' : ['홍길동', '홍길동', '김철수', '박영희', '김철수', '김철수', '홍길동'], 'korean' : range(7)}
df1 = pd.DataFrame(dict1)

print('\n# DataFrame 출력 01')
print(df1)

dict2 = {'name' : ['김철수', '홍길동', '심수봉'], 'english' : range(3)}
df2 = pd.DataFrame(dict2)

print('\n# DataFrame 출력 02')
print(df2)

print('\n# merge() 메소드의 on = "name"을 이용하여 테이터 합치기(inner)')
print(pd.merge(df1, df2, how = 'inner', on = 'name'))

print('\n# how = "outer" 라고 명시하면 full outer join 이다')
print(pd.merge(df1, df2, how = 'outer'))

print('\n# 컬럼 이름이 동일하지 않는 경우')
dict3 = {'leftkey' : ['홍길동', '홍긷롱', '김철수', '박영희', '김철수', '김철수', '홍길동'], 'korean' : range(7)}
df3 = pd.DataFrame(dict3)

print('# DataFrame 출력 03')
print(df3)

dict4 = {'rightkey' : ['김철수', '홍길동', '심수봉'], 'english' : range(3)}
df4 = pd.DataFrame(dict4)

print('\n# DataFrame 출력 04')
print(df4)

print('\n# merge() 메소드의 left_on 과 right_on 사용하기')
print(pd.merge(df3, df4, left_on = 'leftkey', right_on = 'rightkey'))

dict1 = {'key1' : ['김철수', '김철수', '박영희'],
         'key2' : ['one', 'two', 'one'],
         'leftval' : [1, 2, 3]}
left = pd.DataFrame(dict1)
print('\n# DataFrame 출력 05')
print(left)

dict2 = {'key1' : ['김철수', '김철수', '박영희', '박영희'],
         'key2' : ['one', 'one', 'one', 'two'],
         'leftval' : [4, 5, 6, 7]}
right = pd.DataFrame(dict2)
print('\n# DataFrame 출력 06')
print(right)

mylist = ['key1', 'key2']  # 조인할 컬럼 리스트
print('\n# 여러 개의 컬럼 병합하기')
print(pd.merge(left, right, on = mylist, how = 'outer'))

print('\n# suffixes 옵션 사용하기')
print(' # 동일한 컬럼 이름 key2에 대하여 접미사를 붙여 준다')
print(pd.merge(left, right, on = 'key1', suffixes = ('_왼쪽', '_오른쪽')))

print('\n# 색인을 이용한 머지 사용하기')
newdf1 = df1.set_index('name')
print(newdf1)

print('\n# df2 동일')
newdf2 = df2.set_index('name')
print(newdf2)

print('\n# 색인을 이용한 병합')
print(pd.merge(newdf1, newdf2, left_index = True, right_index = True, how = 'outer', indicator = True))