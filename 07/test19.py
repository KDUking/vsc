list_a = []#각 반의 리스트를 넣는다
for i in ["A반","B반","C반"]:
    tmplist = []
    for j in ["국어","영어","수학"]:
        tmp = int(input(i+j+"점수:"))
        tmplist.append(tmp)
    list_a.append(tmplist)
print(list_a)

#각 반의 합을 리스트에 넣어서 출력
# c = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(c[0][0])
# print(c[1][1])
list_h = []
for i in range(3):
    s = 0
    for j in range(3):
        s += list_a[i][j]
    list_h.append(s)

print("합:",list_h)
#각 반의 평균을 리스트에 넣어서 출력
list_avg = []
for i in range(3):
    g = list_h[i] /3
    list_avg.append(g)
print("평균:",list_avg)
        