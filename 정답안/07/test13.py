y = 0
for i in range(1, 11):
    if i % 2 == 1:
        y += 1/i
    else:
        y -= 1/i
    print(y)

print("")
n = 0
sign = -1
for i in range(1, 11):
    sign *= -1
    n += sign * 1 / i
    print(n)
print("")

y = 0
for i in range(1, 11):
    y += (1/i) * (-1)**(i+1)
    print(y)