a = "good luck"
print(a[0])

b = ["g","o","o","d"," ","l","u","c","k"]
print(b[0])

c = ("g","o","o","d"," ","l","u","c","k")
print(c[0])
#b = c의 저장방식은 거의 유사하다
#[0~i]index 번호

d = [78, 88, 56]
print(d)

for i in range(3):
    print(d[i], end=" ")
print("")