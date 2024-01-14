tel = {"홍길동":"010-2345-6789", 
       "김말자":"010-3456-1234", 
       "박문순":"010-5791-2654"}

print(list(tel.keys()))

name = input("친구이름:")
print(tel.get(name, "없습니다."))
