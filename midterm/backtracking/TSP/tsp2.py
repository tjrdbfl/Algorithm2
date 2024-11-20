# 백트래킹 - 유망함수 version 1

INF=float('inf')
N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]

# 간단한 휴리스틱을 이용한 가지치키
# 남은 부분이 더 이상 현재까지 찾은 최적해보다 나은 답을 찾을 가능성이 없을 경우
# W[i][:i]: i 번째 도시 이전에 있는 도시들로 가는 비용
# W[i][i+1:] : i+1 번째 도시 이후에 있는 도시들로 가는 비용
# W[i][:i] + W[i][i+1:] : i번째 도시에서 자기 자신을 제외한 다른 도시들로 가는 비용만을 남기기
min_edge=[min(W[i][:i]+W[i][i+1:]) for i in range(N)]
nearest=sorted((W[i][j],i,j) for i in range(N) for j in range(N) if i!=j)

def simple_heuristic(visited):
    return sum(min_edge[i] for i in range(N) if not (visited&(1<<i)))

# promising function
# 1) 지금까지 찾은 최적해보다 더 나빠지면 가지치기
def promising(path,visited,cost):
    if cost+simple_heuristic(visited)>=best:
        return False
    return True

def tour(path,visited,cost):
    global best
    if promising(path,visited,cost): # 유망할 때만 
        here=path[-1]
        if visited==(1<<N)-1:
            best=min(best,cost+W[here][0])
        else:
            for i in range(N):
                next=nearest[here][i]
                if not (visited&(1<<next)):
                    path.append(next)
                    tour(path,visited|(1<<next),cost+W[here][next])
                    path.pop()

tour([0],1<<0,0)
print(best)
