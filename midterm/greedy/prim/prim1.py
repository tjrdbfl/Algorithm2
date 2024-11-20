# Prim's 알고리즘
# MST : Minimum Spanning Tree
# MST 문제를 해결하는 Prim 알고리즘 구현

def prim(n,adj):
    selected=[] # 추가된 간선 저장
    added=[False]*n # 해당 정점이 MST에 포함되어 있는지
    min_weight=[float('inf')]*n # 트리에 인접한 간선 중 해당 정점에 닿는 최소 간선의 가중치
    parent=[-1]*n  # 트리에 인접한 간선 중 해당 정점에 닿는 최소 간선의 정점
    min_weight[0]=parent[0]=0 # 0번 정점을 시작점으로 한다. 
    ret=0 # 간선의 가중치 최소 합

    for _ in range(n):
        u=-1
        for v in range(n): # 아직 트리에 포함되지 않은 정점들 중에서 최소 간선 가중치를 가진 정점 v를 선택하기 위한 조건
            if not added[v] and (u==-1 or min_weight[u]>min_weight[v]):
                u=v
        if parent[u]!=u: # 출발 정점이 아니면
            selected.append((parent[u],u))
        ret+=min_weight[u]
        added[u]=True

        # 선택된 노드와 인접한 노드들의 가중치 업데이트
        for v, weight in adj[u].items():
            if not added[v] and min_weight[v]>weight: # MST에 포함되지 않았다면
                min_weight[v]=weight
                parent[v]=u
                
    return ret,selected


n,m=map(int,input().split())  # n : node 개수, m : edge 개수
adj=[{} for _ in range(n)]

for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=adj[v][u]=w

cost,edges=prim(n,adj)
print(cost)
print(*edges)


