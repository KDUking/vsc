def avg(a, b):
    s = (a+b) / 2
    return s


#함수 호출
n1 = int(input("수입력:"))
n2 = int(input("수입력:"))
r = avg(n1, n2)

print("평균: %.2f" % r)
