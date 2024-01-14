a = []
b = ["국어","영어","수학"]
for i in range(3):
    tmp = int(input(b[i]+" 점수입력:"))
    a.append(tmp)
print(a)

hap = 0
for i in range(3):
    hap += a[i]
avg = hap / 3
print("합: %d 평균: %.2f" % (hap, avg))