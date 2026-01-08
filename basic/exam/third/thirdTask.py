# Q1
def print_score(nums) :
    print(sum(nums) / len(nums))

# Q2
def print_even(nums) :
    for n in nums :
        if n % 2 == 0 : print(n)

# Q3
def make_url(url) :
    print('http://' + url + '.com')

# Q4
def q4(a, b) :
    print(a + str(b))

# Q5
def print_arithmetic_operation(a, oper, b) :
    if oper == '+' : print('%d + %d = %d' % (a, b, a + b))
    elif oper == '-' : print('%d - %d = %d' % (a, b, a - b))
    elif oper == '*' : print('%d * %d = %d' % (a, b, a * b))
    elif oper == '/' : print('%d / %d = %d' % (a, b, a / b))

# Q6
def gugudan(n) :
    result = []
    for i in range(1, 10) :
        result.append(i * int(n))
    print(result)

# Call 2 function
# print_score([1, 2, 3])
# print_even ([1, 3, 2, 10, 12, 11, 15])
# make_url('naver')
# q4('안녕', 3)
# print_arithmetic_operation(3, '/' ,4)
gu = input()
gugudan(gu)