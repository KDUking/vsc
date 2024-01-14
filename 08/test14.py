def rectangle_area(a,b):
    return (a*b)

m = int(input("가로:"))
n = int(input("세로:"))

r = rectangle_area(m,n)
print("가로: %d 세로: %d 넓이:%d" % (m,n,r))