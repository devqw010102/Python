import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
cnt, Png, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'brokenLineExam'
filename = './Book/data/주요발생국가주간동향(4월2째주).csv'

data = pd.read_csv(filename, index_col = '국가')
print(data.columns)

chartdata = data['4월06일']
print(chartdata)
type(chartdata)

plt.plot(chartdata, color = 'blue', linestyle = 'solid', marker = 'o')
# .py 에서 그래프 안보임 -> Jupiter 사용