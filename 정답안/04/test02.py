sec = int(input("초입력:"))
min = sec // 60
second = sec % 60

print("{}초 => {}분 {}초".format(sec, min, second))
