# 백트랙킹 유망함수 version 2

INF=float('inf')
N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]

min_edges=[min(W[i][:i]+W[i][i+1:]) for i in range(N)]
edges=[(W[i][j],i,j) for i in range(N) for j in range(N) if i!=j] 

# 경로 상에서 이미 방문한 도시들 중 일부를 선택해 순서를 바꾸는 방식으로 경로를 최적화
# 2개의 인접한 도시를 골라서 순서를 바꿔보고, 경로가 더 짧으면 가지치기
def path_reverse_pruning(path):
    global dist
    if len(path)<4: # 경로의 길이가 4 미만이면 인접 도시 쌍을 고려할 수 없기 때문에 가지치기를 하지 않고 바로 False를 반환하여 경로가 유망하다고 판단
        return False
    b,q=path[-2:] # path의 마지막 두 도시 b와 q를 선택
    for i in range(len(path)-3): # 마지막 두 도시를 제외하고 순회
        p,a=path[i:i+2]
        if dist[p][a]+dist[b][q] > dist[p][b]+dist[a][q]:  # 순서를 바꾼 경로가 더 짧다면 가지치기 조건을 만족
            return True
        
    return False    

def MST_heuristic(here,visited):
    dset=DisjointSet(N) # MST 먼저 찾기 
    taken=0 # MST의 총비용
    for w,a,b in edges:  # w: a-> b 로 가는 비용, a,b: 도시 인덱스
        if a!=0 and a!=here and (visited*(1<<a)): # 도시 a 가 시작점이 아니고, 현재 위치도 아니고, 이미 방문한 도시일 경우 이 간선을 이용하지 x
            continue
        if b!=0 and b!=here and (visited*(1<<b)):
            continue
        if dset.merge(a,b): # 도시 a,b 가 서로 아직 같은 그룹으로 연결되어 있지 않은 경우 이 두 도시를 MST 에 추가 
            taken+=w 
    return taken

def promising(path,visited,cost):
    # 지나온 경로를 이용한 가지치기
    if path_reverse_pruning(path):
        return False
    # MST 휴리스틱으로 가지치기
    if best<=cost+MST_heuristic(path[-1],visited):
        return False
    return True

def tour(path,visited, cost):
    global best
    if promising(path,visited,cost):
        here=path[-1]
        if visited==(1<<N)-1:
            best=min(best,cost+W[here][0])
        else:
            for i in range(N):
                next=edges[here][i]
                if not (visited&(1<<next)):
                    path.append(next)
                    tour(path,visited|(1<<next),cost+W[here][next])
                    path.pop()

tour([0],(1<<0),0)
print(best)

