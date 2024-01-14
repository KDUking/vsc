aa = []
bb = []
value = 0

for i in range(100):
    aa.append(value)
    value += 2 # 2의 배수

print(aa)
for i in range(100):
    print(aa[i], end=" ")
print("")

print(aa.index(198))
#역순 대입
for i in range(0, 100):
    bb.append(aa[99-i])

print(bb)