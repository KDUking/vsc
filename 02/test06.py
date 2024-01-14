#1~100 모든 짝수를 구하여라
for i in range(1, 101):
    if i % 2 == 0: #짝수인가요?
        print(i, end=" ")
        
#1~100 모든 짝수의 합을 구하여라
s = 0 #원칙:반드시 초기화 시켜야함(처음값을 설정해준다)
for i in range(1, 101):
    if i % 2 == 0:
        s = s + i
print("합",s)