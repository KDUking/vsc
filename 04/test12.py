a = "파이썬은완전재미있어요"

for i in range(len(a)):
    if i % 2 == 1:
        print("#",end="")
    if i % 2 == 0:
        print(a[i],end="")
print("")