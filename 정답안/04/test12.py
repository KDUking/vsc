a = "파이썬은완전재미있어요"

for i in range(len(a)):
    if i % 2 == 1: # 홀수 자리인가요?
        print("#", end="")
    if i % 2 == 0: # 짝수 자리인가요?
        print(a[i], end="")
print("")