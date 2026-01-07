import numpy as np
import pandas as pd

myIndex = ['김구', '이봉창', '안중근', '윤봉길']
myColumns = ['강남구', '은평구' ,'마포구', '용산구']
mylist = list(10 * onedata for onedata in range(1, 17))
myframe = pd.DataFrame(np.reshape(mylist, (4, 4)), index = myIndex, columns = myColumns)

print(myframe.iloc[1])
print('-'*30)
print(myframe.iloc[[1, 3]])
print('-'*30)
print(myframe.loc['윤봉길'])
print('-'*30)
print(myframe.loc[['이봉창', '윤봉길']])
print('-'*30)
print(myframe.loc[['윤봉길'], ['은평구']])
print('-'*30)
print(myframe.loc[['김구', '이봉창'], ['용산구', '은평구']])
print('-'*30)
print(myframe.loc[myframe['은평구'] <= 100])
print('-'*30)
print(myframe.loc[myframe['은평구'] == 100])
print('-'*30)
myframe.loc['김구' : '안중근', '용산구'] = 80
print(myframe)
print('-'*30)
