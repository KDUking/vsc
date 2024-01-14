s = 0
for i in range(3, -4, -1):
    s += i
    print(i, end= " ")
print("")
print("합:", s)

#============================
y = 0
for i in range(1, 11):
    y += 1 / i
    print(y)
# =====================
m = 0
for i in range(1, 11):
    m += i / (i+1)
    print(m)