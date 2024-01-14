# 입력값 있다, 반환값 없다.
def vest(dan):
   for  i in range(1,10):
        print("%d x %d = %d" % (dan,i,dan*i))

d = int(input("단입력:"))


if d >= 1 and d <= 9:
    vest(d)
else:
    print("1~9 입력하세요")

