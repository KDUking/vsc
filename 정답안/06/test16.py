# num = int(input("정수입력:"))
# if num < 100:
#     print(num * 0.9)
# else:
#     print(num * 1.1)

#============================
# a = int(input("수입력:"))
# b = int(input("수입력:"))
# if a + b - b*b >= 0:
#     print(a+b - b*b)
# else:
#     print("음수")

#============================
# num = int(input("정수입력:"))
# if num % 2 == 0 and num % 3 == 0:
#     print("나누어짐")
# else:
#     print("나누어 지지 않음")

#============================
# a = int(input("정수입력:"))
# b = int(input("정수입력:"))
# if a - b > 0:
#     print("a>b")
# elif a - b < 0:
#     print("a<b")
# else:
#     print("a=b")
#============================
year = int(input("연도:"))
if (year % 4 == 0 and year % 100 !=0) or (year % 4 == 0):
    print("윤년")
else:
    print("평년")