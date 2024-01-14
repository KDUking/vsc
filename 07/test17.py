a = []
for i in range(1,10):
    a.append(2*i)

print(a)

b = []
for i in range(2,10):
    tmp = []
    for j in range(1,10):
        tmp.append(i*j)
    b.append(tmp)
print(b)