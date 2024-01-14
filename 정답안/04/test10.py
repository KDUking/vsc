# 문자열 만들어서 각문자 뒤에 *를 붙여서 출력하려한다.

ss = input("문자열 입력:")

sslen = len(ss)  # 문자열 길이

for i in range(sslen):
    print(ss[i]+"*", end="")
print("")