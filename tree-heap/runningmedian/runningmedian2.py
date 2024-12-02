# 최소-힙과 최대-힙으로 해결하기
from heapq import heappush,heappop

MOD=20090711
class RNG:
    def __init__(self,a,b):
        self.seed=1983
        self.a=a
        self.b=b
    
    def next(self):
        ret=self.seed
        self.seed=((self.a*self.seed)%MOD +self.b)%MOD
        return ret

def runningmedian(n,rng):
    max_heap=[] # 중간값보다 작거나 같은 원소를 담는 최대-힙
    min_heap=[] # 중간값보다 크거나 같은 원소를 담는 최소-힙
    ret=0
    for _ in range(n):
        # 1번 불변식 : 최대 힙의 크기는 최소 힙의 크기보다 같거나, 하나 더 크다.
        if len(max_heap)==len(min_heap):
            heappush(max_heap,-rng.next())
        else: # 크기가 같지 않으면 최대-힙이 하나 더 크므로 최소-힙에 추가
            heappush(min_heap,rng.next())
        # 2번 불변식 : 최대-힙의 루트가 최소-힙의 루트보다 작거나 같다.
        if min_heap and max_heap and min_heap[0]<-max_heap[0]:
            a=heappop(max_heap)
            b=heappop(min_heap)
            heappush(max_heap,-b)
            heappush(min_heap,-a)
        ret=(ret+(-max_heap[0]))%MOD
    return ret

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    rng=RNG(a,b)
    print(runningmedian(n,rng))