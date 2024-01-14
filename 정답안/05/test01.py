a = []
b = list()

print(type(a), type(b))

a = [1,2,3,4,5]
print(a)
print(a[0])
for i in range(5):
    print(a[i], end=" ")
print("")

a = ["hello", "python"]
print(a[0])
print(a[0][0])

print(a)
for i in range(2):
    print(a[i], end=" ")
print("")

a = [1,2,"hello",[10,20]]
print(a)
for i in range(len(a)):
    print(a[i], end=" ")
print("")
print(a[3][1])

a = "hello"
print(a[0])