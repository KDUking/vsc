def c_area(r):
    retlist = []
    area = r * r * 3.14
    round = 2 * r * 3.14
    retlist.append(area)
    retlist.append(round)
    return retlist

m = int(input("반지름:"))
r,k = c_area(m)

print("반지름:{} 넓이:{} 둘레:{}".format(m, r, k))