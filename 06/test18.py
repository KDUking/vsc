kor = int(input("국어점수:"))
eng = int(input("영어점수:"))
math = int(input("수학점수:"))

# a = [100,90,80]

sum = kor + eng + math
avg = sum / 3

print("합:%d" % sum,"평균:%.2f" % avg)

# sum = 0
# sum = a[1] + a[2] + a[3]
# avg = sum/3

# print("합:%d", sum,"평균:%.2f", avg)

if avg >= 80:
    print("잘함")
elif avg >= 70 and avg <= 79:
    print("보통")
else:
    print("미흡")