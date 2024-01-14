str = input("문자열 입력:")
print(str)

# park 4개
count = len(str)

for i in range(count):
  print(str[count-(i+1)],end="")
print("")

