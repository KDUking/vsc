a = int(input("국어점수:"))
b = int(input("수학점수:"))
c = int(input("영어점수:"))

d = [a,b,c]

sum=0
for i in range(3):
    sum += d
print(d)

avg = d /3
print(avg)

#a = []
#b = ["국어","영어","수학"]
# for i in range(3):
#    tmp = int(input(b[i]+"점수입력:"))
#    a.append(tmp)
# print(a)
# 
# hap = 0
# for i in range(3):
#     hap += a[i]
# avg = hap / 3
#print("합: %d 평균:%.2f" % hap avg) 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#