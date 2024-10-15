# 시계에 연결된 스위치 
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

def clocksync(clocks):
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
    ret=clocksync(clocks)
    print(ret)