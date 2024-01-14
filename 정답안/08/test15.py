def area(r):
    return r * r * 3.14

m = int(input("반지름:"))
print("반지름: {} 넓이: {}".format(m, area(m)))