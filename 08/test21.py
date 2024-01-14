def m_sum(a,b):
    s = 0
    if a > b:
        for i in range(b,a+1):
            s += i
    elif a < b:
        for i in range(a,b+1):
            s += i
    return s

num1 = int(input("수1:"))
num2 = int(input("수2:"))

r = m_sum(num1,num2)
print("두 수 %d %d 합: %d" % (num1, num2, r))