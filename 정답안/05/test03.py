a = "good"
b = ["g","o","o","d"]
c = ("g","o","o","d")

print(a)
for i in range(4):
    print(a[i], end="")
print("")

print(b)
for i in range(4):
    print(b[i],end="")
print("")

print(c)
for i in range(4):
    print(c[i],end="")
print("")

#a[0] = "K"
b[0] = "K"
print(b)

#c[0] = "K"