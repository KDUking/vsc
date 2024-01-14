str = input("문자열입력:")
#반복문을 이용해서 입력받은 문자열을 출력 문자 한글자 한글자 확인 o => $

for i in range(len(str)):
    #조건문
    if str[i] != "o":  # if문 다음이 참인가요?
        print(str[i], end="")
    else:  # 그렇지 않다면
        print("$", end="")
print("")

print(str.replace("o", "$"))