a = [10,20,30]
b = (10,20,30)
c = "Python"

a[0] = 100
print(a)
#b[0] = 100
#c[0] = "K"
a[1:3] = [200,300]
print(a)
a[0] = "P"
print(a)
a[1:3] = ["Python","hello"]
print(a)