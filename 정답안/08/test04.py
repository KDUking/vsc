def print19(start, end):
    for i in range(start, end+1):
        print(i, end=" ")
    print("")

s = int(input("시작값:"))
e = int(input("끝값:"))

#함수 호출
if s < e:
    print19(s, e)
else:
    print("시작값이 작아야 함")