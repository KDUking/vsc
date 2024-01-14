s = "#"
print(s,s,s, sep="")
print(s+s+s)
print(s*3)

for i in range(3):
    print(s,end="")
for i in range(4):
    print(s,end="")
print("")

print("%s %s %s" % (s, s, s))