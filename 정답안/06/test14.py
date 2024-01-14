score = []
a = ["국어","영어","수학"]
for i in range(3):
    tmp = int(input(a[i]+" 점수입력:"))
    score.append(tmp)
print(score)

s = 0
for i in range(3):
    s += score[i]  # 누적합

avg = s / len(score)

print("합: %d 평균: %.2f" % (s, avg))

if avg >= 80:
    print("잘함")
elif 70 <= avg <80:
    print("보통")
else:
    print("미흡")