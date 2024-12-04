# 하한과 상한 범위 내의 가중치만 이용한 dfs 탐색 
def dfs(here,lo,hi):
    if here==n-1: # dfs 탐색으로 마지막 노드에 도달했을 때 
        return True
    else:
        visited[here]=True
        for there,weigth in adj[here].items():
            if not visited[there] and (lo<=weigth<=hi):
                if dfs(there,lo,hi): # dfs 탐색으로 마지막 노드에 도달했을 때 
                    return True 
        return False

# DFS 로 0번 정점에서 n-1 번 정점으로 가는 경로가 존재하는 지 확인
def has_path(lo,hi):
    global visited
    visited=[False]*n
    return dfs(0,lo,hi)

# 모든 가능한 (하한, 상한) 의 쌍에 대해 경로가 존재하는지 전부 확인
def min_diff():
    ret=INF
    for lo in range(len(weights)):
        for hi in range(lo+1,len(weights)):
            if has_path(weights[lo],weights[hi]):
                ret=min(ret,weights[hi]-weights[lo])
                break
    return ret

def tpath():
    global weights,adj
    adj=[{} for _ in range(n)]
    for a,b,w in edges:
        adj[a][b]=adj[b][a]=w
    weights={edges[i][2] for i in range(m)}
    weights=sorted(list(weights))
    return min_diff()

INF=float('inf')
for _ in range(int(input())):
    n,m=map(int,input().split())
    edges=[list(map(int,input().split())) for _ in range(m)]
    ret=tpath()
    print(0 if ret==INF else ret)

# n=5, m=6
# edges = [
#     [0, 1, 4], 
#     [1, 2, 5], 
#     [0, 3, 7], 
#     [3, 4, 8], 
#     [1, 3, 6], 
#     [2, 4, 9]
# ]

# adj = [
#     {1: 4, 3: 7},    # 노드 0과 연결된 노드들: (1, 가중치 4), (3, 가중치 7)
#     {0: 4, 2: 5, 3: 6}, # 노드 1과 연결된 노드들: (0, 가중치 4), (2, 가중치 5), (3, 가중치 6)
#     {1: 5, 4: 9},    # 노드 2와 연결된 노드들: (1, 가중치 5), (4, 가중치 9)
#     {0: 7, 1: 6, 4: 8}, # 노드 3과 연결된 노드들: (0, 가중치 7), (1, 가중치 6), (4, 가중치 8)
#     {3: 8, 2: 9}     # 노드 4와 연결된 노드들: (3, 가중치 8), (2, 가중치 9)
# ]