def secret_map(n, arr1, arr2):
    answer = []
    for i in range(n):
        combined = arr1[i] | arr2[i]

        binary_row = bin(combined)[2:].zfill(n)
        row_string = binary_row.replace('1', '#').replace('0', ' ')
        answer.append(row_string)

    return answer

print(secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# Programmers
# 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도

# 1. 비트 연산 : line 4
# 2. .zfill : 2진수 변환 이후 자릿수 맞추기