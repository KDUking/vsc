subject = ["국어","영어","수학","과학","한국사"]
for i in subject:
    print(i, end=" ")
print("")

# 구구단 2단 출력
for i in range(1, 10):
    print(2*i, end= " ")
print("")

# 2 ~ 9단 출력  중첩 for문
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end= " ")
    print("") # 줄바꿈

name = ["홍길동", "임꺽정"]
subject = ["국어","영어","수학"]

for i in name:
    for j in subject:
        print("%s %s" % (i, j))