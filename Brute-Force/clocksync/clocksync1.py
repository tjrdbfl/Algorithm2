# 재귀적 완전탐색(DFS)로 해결 
import sys

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

INF=31 # 스위치 개수 10개 * 최대 3번까지 누를 수 있다

# 모두 12시가 되었는지 확인 (원소가 모두 0인지 확인)
def aliagned(clocks):
    return not any(clocks)  # clock이 모두 0을 가리키면 True 반환

def push(clocks,switch):
    for clock in linked[switch]:
        clocks[clock]=(clocks[clock]+1)%4

def clocksync(clocks,switch):
    if switch==10: # 모든 스위치를 눌렀다
        return 0 if aliagned(clocks) else INF # 더 이상 스위치를 누를 필요가 없으므로 0을 반환
    else:
        ret=INF
        for cnt in range(4):
            ret=min(ret,cnt+clocksync(clocks,switch+1))
            push(clocks,switch)
        return ret

input=sys.stdin.readline
for _ in range(int(input())):
    clocks=[(int(x)//3)%4 for x in input().split()]
    mincnt=clocksync(clocks,0) # 0번 스위치 부터 시작
    print(mincnt if mincnt<31 else -1)
