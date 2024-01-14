# 넓이 둘레를 반환하는 함수
def rect(width, height):
    area = width * height
    round = 2 * (width + height)
    return area, round  # ?  모든언어에서 반환값은 오직 한개.

w = int(input("가로:"))
h = int(input("세로:"))

# 함수 호출
r, k = rect(w, h)

print("결과:", r, k)
print(type(r))
print(type(k))
 