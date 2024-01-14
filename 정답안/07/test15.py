# 2단 리스트에 넣어서 출력
a = []
for i in range(1, 10):
    a.append(2*i)

print(a)

gugu = []
for i in range(2, 10):
    tmp = []
    for j in range(1, 10):
        tmp.append(i*j)
    gugu.append(tmp)

print(gugu)