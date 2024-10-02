import sys

# 모듈러 연산 적용 => 더 빠름. 큰 수의 덧셈이 사려져서 
def tiling(n):
    if n<=2:
        return n
    else:
        a,b=1,2
        for i in range(2,n+1):
            a,b=b,(a+b)%MOD
        return b

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    print(tiling(n))