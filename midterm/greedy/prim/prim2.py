# 우선순위 큐를 사용하는 Prim 알고리즘
from heapq import heapify,heappop,heappush

def prim(n,adj):
    selected=[]
    added=[False]*n
    ret=0
    pq=[(0,0,-1)] # (가중치=0,출발정점=0,부모=-1)

    while pq:
        w,u,p=heappop(pq)
        if not added[u]:
            added[u]=True
            if p!=-1: # 출발 정점을 제외한 간선 추가
                selected.append((p,u))
            ret+=w
            
            for v,weight in adj[u].items():
                if not added[v]: # 모든 방문하지 않은 이웃 노드의 간선 정보를 우선순위 큐에 추가
                    heappush(pq,(weight,v,u))

    return ret,selected

n,m=map(int,input().split())  # n : node 개수, m : edge 개수
adj=[{} for _ in range(n)]

for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=adj[v][u]=w

cost,edges=prim(n,adj)
print(cost)
print(*edges)
