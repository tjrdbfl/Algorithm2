# 중복 순열을 이용하여 풀기
import sys
from itertools import product

linked={
    0:[0,1,2],
    1:[3,7,9,11],
    2:[4,10,14,15],
    3:[0,4,5,6,7],
    4:[6,7,8,10,12],
    5:[0,2,14,15],
    6:[3,14,15],
    7:[4,5,7,14,15],
    8:[1,2,3,4,5],
    9:[3,4,5,9,13],
}

INF=31

def check(clocks):
    return not any(clocks)

def push(clocks,switch,cnt):
    for clock in linked[switch]:
        clocks[clock]=(clocks[clock]+cnt)%4

# prod = (0, 1, 2, 3, 0, 1, 2, 3, 0, 1)
def clocksync(clocks):
    ret=INF
    for prod in product(range(4),repeat=10): # 0~9 스위치가지 각각 0번, 1번, 2번, 3번 누르는 조합을 모두 생성
        pushed=clocks[:] # 원래 시계 정보
        for switch in range(10):
            push(pushed,switch,prod[switch])
        if check(pushed):
            ret=min(ret,sum(prod))
    return ret

input=sys.stdin.readline

for _ in range(int(input())):
    clocks=[(int(x)//3)%4 for x in input().split()]
    ret=clocksync(clocks)
    print(ret if ret<INF else -1)