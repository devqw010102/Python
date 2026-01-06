def secret_map(n, arr1, arr2):

    a = []
    b = []
    for number in arr1:
        a.append(format(number, '0%db' % n))
    for number in arr2:
        b.append(format(number, '0%db' % n))
    print(a)
    print(b)

    for n1, n2 in zip(a, b):
        print(n1, n2)



print(secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# Programmers
# 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도