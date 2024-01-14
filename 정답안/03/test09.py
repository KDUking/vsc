odd = 1+3+5+7+9

s = 0
for i in range(1, 101):
    if i % 2 == 1:  # == 관계연산자: True / False
        s = s + i  # 누적합
print("")

print(s)