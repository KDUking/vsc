s = 0
n = 2 #초기식
while n <= 10:
    s += n
    n += 2
print("짝수합:",s)

s = 0
n = 9 #초기식
while n >= 1:
    s += n
    n -= 2 #증감식
print("홀수합:",s)