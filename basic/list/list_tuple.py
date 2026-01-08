## list, tuple : 자바의 배열과 같음

# list : 배열의 요소(값) 수정, 추가
movieList = ['닥터 스트레인지', '스플릿', '럭키']


# tuple : 배열의 요소(값) 수정, 추가 불가능
movieTuple = ('닥터 스트레인지', '스플릿', '럭키')

movieList.append('배트맨')
movieList[3] = '배트맨3'

## 삭제
# movieList.pop(2)
del movieList[2]

print('movieList : ' , end='')
for movie in movieList:
    print(movie, end=' ')

print('\n----------')

## 추가, 수정, 삭제
# movieTuple.append('배트맨')
# movieTuple[3] = '배트맨3'
# del movieTuple[2]

print('movieTuple : ' , end='')
for movie in movieTuple:
    print(movie, end = ' ')

print('\n----------')

# 리스트 값 합계, 평균, 최대값, 최소값
score = [65, 73, 84, 98, 70]

print('합계 : %d' %(sum(score)))
print('최소값 : %s' %(min(score)))
print('최대값 : %s' %(max(score)))
print('평균 : %s' %(sum(score) / len(score)))