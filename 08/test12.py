def maxnum(a,b):
    if a > b:
        ma = a
    elif a < b:
        ma = b
    return ma

m1 = int(input("수1:"))
m2 = int(input("수2:"))

r = maxnum(m1,m2)
print("큰 값: {}".format(r))
