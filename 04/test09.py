a = "good luck"
print(a)
#반복문을 사용해서 출력가능할까요?

for i in range(len(a)):
    print(a[i], end="")
print("")

#문자열과 컬렉션 자료형은 메모리에 저장되는 방식이 거의 동일하다.
#컬렉션 자료형:저장공간 1개 그런데 여러개를 저장할 수 있는 자료형

print(a[8])
print(a[-1])

#슬라이싱:문자열을 입력 받아서 문자열의 일부분 추출하는 방법
print(a[0:4])
print(a[:4])
print(a[5:])

b = ["g","o","o","d"," ","l","u","c","k"]
print(b[:4])
print(b[5:])