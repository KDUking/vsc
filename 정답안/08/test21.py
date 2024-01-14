def pnz(a):
    if a > 0:
        r = 1
    elif a < 0:
        r = -1
    else:
        r = 0
    return r

while True:
    num = int(input("수입력:"))
    k = pnz(num)
    if k == 1:
        print("양수")
    elif k == -1:
        print("음수")
    else:
        print("0")
        break