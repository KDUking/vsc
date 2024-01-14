# 1 ~ 10 홀수합
print(1 + 3 + 5 + 7 + 9)

# 1 ~ 100 합 : 반복문?

sum = 0
for i in range(1, 101):
    sum = sum + i

print(sum)

sum = 0
for i in range(5, 11):
    sum = sum + i  # 누적합

print(sum)