# 변화하는 중간값 찾기
# 정렬 + BST 로 해결하기 
# output : 각 테스트 케이스의 중간값의 합을 MOD로 나눈 나머지 
# 수열의 길이가 짝수일 경우, 가운데 있는 두 값 중 보다 작은 것 
import bisect

MOD=20090711
class RNG:
    def __init__(self,a,b):
        self.seed=1983
        self.a=a
        self.b=b
    
    def next(self):
        ret=self.seed
        self.seed=((self.seed*self.a)%MOD+self.b)%MOD
        return ret

def runningmedian(n,rng): 
    num=[]
    ret=0
    for k in range(1,n+1):
        next=rng.next()
        bisect.insort(num,next) # 정렬된 리스트 num에 next 삽입
        ret=(ret+num[(k-1)//2])%MOD
    return ret

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    rng=RNG(a,b)
    print(runningmedian(n,rng))