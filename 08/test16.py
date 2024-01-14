def area(r):
    area = r * r * 3.14
    round = 2 * 3.14 * r
    return area,round

m = int(input("반지름:"))
print("반지름:{} 넓이:{}".format(m,area(m)))

