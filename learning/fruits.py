# 데이터 저장
import pandas as pd
import numpy as np

# 엑셀 데이터 불러오기
df = pd.read_excel('learning/data/사과배복숭아-학습.xlsx')
print(df)

# 결측치 값의 유무 확인
print(df.isna().sum())  # result : Color Column 49 units

# 모든 결측치 값을 0으로 대체
df.fillna(0, inplace = True)
print(df.isna().sum())

# fruit Column 의 항목값 별 개수
print(df['fruit'].value_counts())

# 사과 0, 배 1, 복숭아 2
df.replace({'fruit' : {'사과' : 0, '배' : 1, '복숭아' : 2}}, inplace=True)

print(df)