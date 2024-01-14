y = 0

for i in range(1,11):
    y += i+1 / i
    print(y)
#=======================

y = 0
for i in range(1,11):
    if i % 2 == i:
        y += 1/i
    else:
        y -= 1/i
    print(y)
#======================

y = 0
sign = -1
for i in range(1,11):
    sign *= -1
    y += sign * 1 / i
    print(y)
print("")
#======================

y = 0
for  i in range(1,11):
    y += (1/i) * (-1)**(i+1)
    print(y)