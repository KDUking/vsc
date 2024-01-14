a = []
b = ["돼지", "닭", "토끼"]
for i in range(3):
    tmp = int(input(b[i]+" 가축수:"))
    a.append(tmp)

print(a)

l = [4, 2, 4]
s = 0
for i in range(3):
    s += a[i] * l[i]

print("다리합:", s)