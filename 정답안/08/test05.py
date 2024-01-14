# return 예약어 사용하는 함수 (반환값이 있는 함수)
#함수 선언/정의
def fadd(l, m, n):
    s = l + m + n
    return s

#함수 호출
r = fadd(23, 34, 5)

# 결과 확인
print("세 수의 합: %d" % r)