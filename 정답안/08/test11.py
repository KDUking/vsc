def maxNum(num1, num2):
    if num1 > num2:
        ma = num1
    elif num1 < num2:
        ma = num2
    return ma

m1 = int(input("수1:"))
m2 = int(input("수2:"))

#함수 호출
r = maxNum(m1, m2)

print("큰값: {}".format(r))