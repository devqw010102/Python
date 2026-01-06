def cola(a, b, n):
    answer = 0

    while n >= a:
        new =  (n // a) * b
        remain = n % a

        answer += new
        n = new + remain
    return answer


print(cola(2, 1, 20))