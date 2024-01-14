def one2n_sum(a):
    result = 0
    for i in range(1, a+1):
        result += i
    return result

num = int(input("수입력:"))
# if num >= 1:
#     r = one2n_sum(num)
#     print("합: %d" % r)
# else:
#     print("1보다 작습니다.")

if num < 1 or num > 10:
    print("입력범위초과:")
else:
    numt = num * 10
    print("1 ~ %d까지 합: %d" % (numt,one2n_sum(numt)))
