# 넓이 둘레를 반환하는 함수
def rect(a,b):
    area = a * b
    round = (a+b) * 2
    return area, round # ? 모든언어에서 반환값은 오직 한개.

w = int(input("가로:"))
h = int(input("세로:"))

r,k= rect(w,h)
print("결과:", r,k)
print(type(r),type(k))