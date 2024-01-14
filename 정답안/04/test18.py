# random함수에 관하여
import random

#리스트
a = ["red", "blue", "green", "purple"]
#print(type(a))
print(random.choice(a))
print(random.randint(1, 3))
print(random.randrange(1, 3))
random.shuffle(a)
print(a)
print(random.random())  # 0 ~ 1 사이의 실수값 출력
