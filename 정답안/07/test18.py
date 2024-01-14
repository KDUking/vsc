for i in range(1, 6): # 줄수
    for j in range(1, 5):
        print(j, end="")
    print("")  #줄바꿈
print("")
#=========================
for i in range(1, 6): #줄수
    for j in range(1, 5):
        print(i+j-1, end="")
    print("")
#-----------
for i in range(5):
    for j in range(i+1, i+5):
        print(j, end="")
    print("")