sum = 0
for i in range(1, 101):
    sum += i
print(sum)

sum = 0
for i in range(1, 101, 2):
    sum += i
print("홀수합:", sum)

sum = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum += i
print("홀수합:", sum)

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue
    sum += i
print("홀수합:", sum)

s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        s += i
    i += 1
print("홀수합:", s)