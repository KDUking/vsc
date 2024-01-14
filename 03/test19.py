# sco1 = int(input("국어:"))
# sco2 = int(input("영어:"))
# sco3 = int(input("수학:"))

# sum = sco1 + sco2 + sco3 # 반복문 x  ==> 컬렉션 자료형
# avg = sum / 3
# print("합: %d 평균: %.2f" % (sum , avg))


#컬렉션 자료형:저장공간 1개 그 안에 여러개를 저장할 수 있는 형태
#리스트 [],튜플 (),딕셔너리 {},세트 {}

score = [78, 89, 97]#리스트
print(score)
print(score[0])#컬렉션 자료형의 원소값을 출력하는 기호 index
print(score[1])
print(score[2])
#합과 평균을 구해보자

sum = score [0] + score [1] + score [2]
avg = sum / 3

print("합:%d , 평균:%.2f" % (sum, avg))


