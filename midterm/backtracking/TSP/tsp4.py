# 메모이제이션으로 풀기
INF=float('inf')
N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]
cache=[[-1]*(i+1) for i in range(N)]

def tour(here,visited):
    if visited==(1<<N)-1:
        return W[here][0]
    elif cache[here][visited]!=-1:
        return cache[here][visited]
    else:
        ret=INF
        for i in range(N):
            if not (visited&(1<<i)):
                ret=min(ret,W[here][i] + tour(i,visited|(1<<i)))
        
        cache[here][visited]=ret

        return cache[here][visited]

tour([0],(1<<0))

