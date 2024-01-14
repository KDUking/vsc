sco1 = int(input("국어:"))
sco2 = int(input("영어:"))
sco3 = int(input("수학:"))

score = [sco1,sco2,sco3]
print(score)
print(score[0])
print(score[1])
print(score[2])

sum = score [0] + score [1] + score [2]
avg = sum / 3

print("합:%d , 평균:%.2f" % (sum, avg))

#s = 0
#for i in range(len(score)):
#    s += a[i] #누적합
#avg = s / len(score)
#print("합:%d 평균:%.2f" % (s,avg))
