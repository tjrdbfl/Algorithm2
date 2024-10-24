def promising(path,visited,cost):
    if best<=cost:
        return False
    return True

def tour(path,visited,cost):
    global best
    if promising(path,visited,cost): # 유망하지 않으면 가지치기
        here=path[-1]
    if visited==(1<<N)-1:  # 모든 노드를 방문했을 때 
        best=min(best,cost+W[here][0]) # 최적값 업데이트
    else:
        for i in range(N):
            if not (visited&(1<<i)): # 방문하지 않은 정점 모두 시도
                path.append(i)
                tour(path,visited|(1<<i),cost+W[here][i])
                path.pop()

def tour1(here,visited):
    global cache
    if visited==(1<<N)-1:
        return W[here][0]
    elif cache[here][visited]!=-1:
        return cache[here][visited]
    else:
        ret=INF
        for there in range(N):
            if not (visited&(1<<there)):
                ret=min(ret,W[here][there]+tour1(there,visited|(1<<there)))
        cache[here][visited]=ret
        return cache[here][visited]

INF=float('inf')
N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]
cache=[[-1]*(i+1) for i in range(N)]
print(tour1([0],1<<0))