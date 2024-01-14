def one_sum(a):
    s= 0
    if a > 0:
        for i in range(1, a+1):
            s += i
    elif a < 0:
        for i in range(-1, a-1, -1):
            s += i
    return s

num = int(input("수입력:"))
if num == 0:
    print("입력수가 0입니다.")
else:
    r = one_sum(num)
    print("입력수:", num, "합:", r)