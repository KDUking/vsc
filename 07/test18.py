a = []
for i in ["국어","영어","수학"]:
    b = int(input(i + "점수입력:"))
    a.append(b)
print(a)

s = 0
for i  in range(len(a)):
    s += a[i]
print("합:%d 평균:%.2f" % (s, s/ len(a)))
