n = 1  # 초기식
s = 0
while n <= 10:  # 조건식
    if n % 2 == 0:
        s += n
        print("n: %d s: %d" % (n, s))
    n += 1  # 증감식
print("s: %d" % s)
