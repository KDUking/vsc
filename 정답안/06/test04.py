# 딕셔너리 조작함수 get()
name = {100:"황복동", 200:"황채연", 300:"황나연"}
print(name)
print(name[100])
# print(name[400])

print(name.get(100, "없습니다."))
print(name.get(400, "없습니다."))

#pop()
print(name.pop(100))
print(name)
del(name[200])
print(name)
