def pzn(n):
    if n > 0:
        r = 1
    elif n < 0:
        r = -1
    else:
        r = 0
    return r

while True:
    num = int(input("수입력:"))
    k = pzn(num)
    if k == 1:
        print("양수")
    elif k == -1:
        print("음수")
    else:
        print("0")
        break