aa = []
for i in range(4):
    aa.append(0)

print(aa)

# aa[0] = int(input("1번째 정수:"))
# aa[1] = int(input("2번째 정수:"))
# aa[2] = int(input("3번째 정수:"))
# aa[3] = int(input("4번째 정수:"))
# print(aa)

#반복문
for i in range(4):
    aa[i] = int(input(str(i+1)+"번째 정수:"))

# hap = aa[0] + aa[1] + aa[2] + aa[3]
# print("합: %d" % hap)
hap = 0
for i in range(4):
    hap += aa[i]
print("합: %d" % hap)
