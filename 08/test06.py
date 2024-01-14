def avg(a,b):
    s = (a+b) / 2
    return s

n1 = int(input("수입력:"))
n2 = int(input("수입력:"))

r = avg(n1,n2)

print("두 수의 평균: %.2f" % r)