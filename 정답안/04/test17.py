# num = input("수입력:")
# num = int(num)
# print(num + 6)

#=======================
k1 = int(input("국어:"))
k2 = int(input("영어:"))
k3 = int(input("수학:"))

sum = k1 + k2 + k3 # 반복문 x
avg = sum / 3
print("총점: %d 평균: %.2f"  % (sum, avg))

# 컬렉션 자료형
a = [45, 78, 99]

s = 0
for i in range(len(a)):
    s += a[i]  # 누적합
avg = s / len(a)
print("합: %d 평균: %.2f" % (s, avg))
