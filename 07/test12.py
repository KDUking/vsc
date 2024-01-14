s = 0
for i in range(1,101):
    s += i
print(s)
print("")

s = 0 #스탭
for i in range(1,101,2):
    s += i
print("홀수합:",s)
print("")

s = 0
for i in range(1,101):
    if i % 2 == 1:
        s += i
print("홀수합:",s)
print("")

s = 0
for i in range(1,101):
    if i % 2 == 0:
        continue
    s += i
print("홀수합:",s)
print("")

s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        s += i
    i += 1
print("홀수합:",s)