for i in range(1, 101):
    if i % 2 == 0: # 짝수인가요?
        print(i, end= " ")
print("")

s = 0
for i in range(1, 101):
    if i % 2 == 0:
        s = s + i

print("짝수합", s)