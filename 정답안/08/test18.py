def one2nt(n):
    s = 0
    for i in range(1, 10*n+1):
        s += i
    return s

num = int(input("자연수:"))
if num < 1 or num > 10:
    print("입력범위 초과")
else:
    print("1 ~ %d까지 합: %d" % (num*10, one2nt(num)))