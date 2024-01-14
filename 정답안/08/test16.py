def c_area(r):
    retList = []
    area = r * r * 3.14
    round = 2 * r * 3.14
    retList.append(area)
    retList.append(round)
    return retList

m = int(input("반지름:"))
r, k = c_area(m)

print("반지름:{} 넓이:{} 둘레:{}".format(m, r, k))