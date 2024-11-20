from heapq import heappush,heappop,heapify

# 최소 비용의 경우
def strjoin(strlen):
    heapify(strlen) # 우선순위 큐 만들기
    ret=0
    while len(strlen)>1: # 원소가 1개 남을 때까지
        len1=heappop(strlen)
        len2=heappop(strlen)
        heappush(strlen,len1+len2)
        ret+=len1+len2

    return ret

# 최대 비용의 경우
def strjoin1(strlen):
    strlen=[-x for x in strlen] # 음수로 넣기 
    heapify(strlen)
    ret=0
    while len(strlen)>1:
        len1=-heappop(strlen)
        len2=-heappop(strlen)
        heappush(strlen,-(len1+len2))
        ret+=len1+len2    
    return ret


for _ in range(int(input())):
    n=int(input())
    strlen=list(map(int,input().split()))
    print(strjoin(strlen))
