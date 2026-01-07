import pandas as pd

myIndex = ['마포구', '용산구', '서대문구' ,'동대문구', '은평구', '구로구' ,'강서구']
mylist = [40, 80, 70, 50, 60, 30, 20]
mySeries = pd.Series(data = mylist, index = myIndex)

# '은평구' 만 조회
print(mySeries[['은평구']])

# '서대문구' 부터 '구로구' 까지 조회
print(mySeries['서대문구' : '구로구'])

# '용산구' 와 '동대문구'만 조회
print(mySeries[['용산구','동대문구']])

# 2번째 요소만 조회
print(mySeries.iloc[2])

# 0, 2, 4 번째 데이터 조회
print(mySeries[0 : 5 : 2])

# 1, 3, 4 번째 데이터 조회
print(mySeries.iloc[[1, 3, 4]])

# 슬라이싱을 사용하여 2번째 ~ 4번째 조회
print(mySeries[2 : 5 :])

# 2번째 항목의 값을 99로 변경
mySeries.iloc[2] = 99
print(mySeries)

# 2번째 부터 4번째 까지 66으로 변경
mySeries.iloc[2 : 5 :] = 66
print(mySeries)

# '마포구'와 '강서구'만 55로 변경
mySeries[['마포구','강서구']] = 55
print(mySeries)

# 짝수 행만 77로 변경
mySeries[0 : : 2] = 77
print(mySeries)

# 최종 결과를 확인
print(mySeries)