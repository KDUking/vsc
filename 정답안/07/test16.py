# 3 * 1 : 일차원 리스트
score = []
for i in ["국어", "영어", "수학"]:
    tmp = int(input(i+ " 점수입력:"))
    score.append(tmp)

print(score)

s = 0
for i in range(len(score)):
    s += score[i]
print("합: %d 평균: %.2f" % (s, s/len(score)))