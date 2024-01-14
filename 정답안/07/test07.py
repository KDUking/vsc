# break / continue
a = [1,2,3,4,5]
for i in a:
    if i == 4:
        break
    if i % 2 == 0:
        continue
    print(i, end= " ")
print("")
print("최종 i값:", i)