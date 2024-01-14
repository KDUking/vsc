a = "good luck"
print(a)
#반복문을 사용해서 출력가능할까요?
#문자 한글자 한글자 출력
for i in range(len(a)):
    print(a[i], end="")
print("")

#문자열과 컬렉션 자료형은 메모리에 저장되는 방식이 거의 동일하다.
#컬렉션 자료형: 저장공간 1개 그런데 여러개를 저장할 수 있는 자료형

print(a[8])
print(a[-1])
print(a[:4])
print(a[5:])

b = ["g","o","o","d"," ","l","u","c","k"]
print(b[:4])
print(b[5:])