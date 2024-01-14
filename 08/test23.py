def fc(temper,action):
    if action == 0:
        tmp = temper *1.8 + 32
        tmpact = "C2F"
    elif action == 1:
        tmp = (temper - 32) / 1.8
        tmpact = "F2C"
    return tmp,tmpact # 튜플 반환

tm = int(input("온도:"))
t = int(input("화씨:1 , 섭씨:0 =>"))

(rt , ra) = fc(tm, t)

print("{} : {} => {}".format(ra,tm,rt))