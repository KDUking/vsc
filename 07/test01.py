#for문 컬렉션 자료형으로 반복문(리스트)

for i in [1,2,3,4,5]:
    print("파이썬")
print("")

for i in ["a","b","c"]:
    print("리스트")
print("")

for i in [1,2,3,"a","b","c",[10,20]]:
    print("반복문")
print("")

for i in (1,2,3,4,5):
    print("튜플")
print("")

#딕셔너리/세트(순서가 없는 자료형)

for i in {1:"a",2:"b",3:"c"}:
    print(i, "딕셔너리")
print("")

for i in {2,3,3,3,3,3,1}:
    print(i,"세트")
print("")

for i in "Python":
    print(i)
print("")