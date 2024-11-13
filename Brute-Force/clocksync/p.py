# 2
# 12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
# 12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6 

# 어떤 스위치건 최대 3번만 누르면 12시로 맞추어진다. 
INF=31 # 최대 30(10*3)번 까지 눌러볼 수 있다. 

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

sequence=[
    (8,linked[4]),
    (11,linked[1]),
    (13,linked[9]),
    (6,linked[3]),
    (10,linked[2]),
    (7,linked[7]),
    (4,linked[8]),
    (1,linked[0]),
    (3,linked[6]),
    (0,linked[5]),
]

def aligned(clocks):
    return not any(clocks) # 하나라도 1이상의 숫자가 있으면 True -> False

def push(clocks,switch):
    for clock in linked[switch]:
        clocks[clock]=(clocks[clock]+1)%4

def clocksync(clocks,switch):
    if switch==10:
        return 0 if aligned(clocks) else INF
    else:
        ret=INF
        for cnt in range(4):
            ret=min(ret,cnt+clocksync(clocks,switch+1))
            push(clocks,switch)
        return ret 

def push2(pushed,switch,cnt):
    for clock in linked[switch]:
        pushed[clock]=(pushed[clock]+cnt)%4


def clocksync2(clocks):
    for prod in product(range(4),repeat=10):
        pushed=clocks[:]
        for switch in range(10):
            push2(pushed,switch,prod[switch])
        if aligned(pushed):
            ret=min(ret,sum(prod))
    return ret

def clocksync3(clocks):
    ret=0
    for clock,linked_clock in sequence:
        cnt=(4-clocks[clock])%4
        for link in linked_clock:
            clocks[link]=(clocks[link]+cnt)%4
        ret+=cnt    

    return -1 if any(clocks) else ret


input=sys.stdin.readline
for _ in range(int(input())):
    clocks=[(int(x)//3)%4 for x in input().split()]
    mincnt=clocksync(clocks,0)
    print(mincnt if mincnt<INF else -1)
