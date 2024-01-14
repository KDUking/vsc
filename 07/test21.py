# s = 0
# while True:
#     num = int(input("정수입력:"))
#     if num == 0:
#         break
#     s += num
# print("합",s)


s = 0
n = int(input("정수입력:"))
while n != 0:
    s += n
    n = int(input("정수입력:"))
print("합:",s)