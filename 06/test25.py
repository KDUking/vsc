year = int(input("연도입력:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("윤년")
else:
    print("평년")