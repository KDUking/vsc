print("1+3+5+7+9 =", 1+3+5+7+9)

#1~100 모든 수를 출력해보자
for i in range(1,101):
    print(i,end=" ")
print(" ")

#1~100 모든 수의 합을 출력해보자    
s = 0
for i in range(1,101):
    s = s + i #누적합
print("합",s)

#1~100 모든 홀수를 출력해보자 (조건문 예습)
for i in range(1, 101):
    if i % 2 == 1: #홀수 인가요?
        print(i, end=" ")

#1~100 모든 홀수의 합을 구해보자
s = 0
for i in range(1, 101):
    if i % 2 == 1:
        s = s + i
print("합",s)
#관계연산자: true/false
print(1==2)
print(1==1)