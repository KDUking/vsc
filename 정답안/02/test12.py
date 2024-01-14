name = input("이름:")
year = int(input("출생연도:"))

print("이름:", name, "출생연도:", year)
print("이름: %s 출생연도: %d" % (name, year))
print("이름: {} 출생연도: {}".format(name, year))
