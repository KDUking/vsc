cock = int(input("닭:"))
rabbit = int(input("토끼:"))
pig = int(input("돼지:"))

a = [12,8,14]
for i in range(30):
    tmp = int(input(a[i] + "다리:"))

sum =cock*2 + rabbit*4 + pig*4
print("다리합:%d" % sum)

#a = []
#b = ["돼지","닭","토끼"] 
#for  i in range(3):
#    tmp = int(input( b[i] + "가축수:"))
#    a.append(tmp)
# print(a)
# 
#l = [4, 2 , 4] 
#s = 0
#for i in range(3):
#   s += a[i] * l[i]
#print("다리합:",s)