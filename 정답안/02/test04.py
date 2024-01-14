print(("#"*3 + "*"*4)*2)


# 중첩 for문
for i in range(2):
    for j in range(3):
        print("#", end="")
    for j in range(4):
        print("*" , end="")
print("")