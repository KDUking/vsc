dan = int(input("단입력:"))
if 2 <= dan <= 9:
    for i in range(1, 10):
        print("%d x %d = %d" %(dan, i, dan*i))
else:
    print("2 ~ 9 입력하세요.")