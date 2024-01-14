ss = input("문자열 입력:")
sslen = len(ss)
for i in range(sslen):
    if i % 2 == 1:
        print(ss[i+"#"],end="")
print("")



#a = "파이썬은완전재미있어요"
#홀수 자리 데이터 #으로 변경
#
#a = ["파","이","썬","은"] o
#a = ("파","이","썬","은") x
#alen = len(a) #문자열 개수
#for i in range(alen):
#   if i % 2 == 1:  #홀수인가요?
#     a[i] = "#"  #문자열의 요소값을 변경하려 했는데....
#
#prin(a)