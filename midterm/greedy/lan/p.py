from heapq import heapify,heappop,heappush

def prim_heap(n,adj):
    selected=[]
    added=[False]*n
    pq=[(0,0,-1)]  # w,u,p
    ret=0

    while pq:
        w,u,p=heappop(pq)
        if not added[u]:
            added[u]=True

            if p!=-1:
                selected.append((p,u))
            ret+=w

            for v,weight in adj[u].items():
                if not added[v]:
                    heappush(pq,(weight,u,v))

    return ret,selected

def prim(n,adj):
    selected=[]
    added=[False]*n
    parent=[-1]*n
    min_weight=[float('inf')]*n
    ret=0

    for _ in range(n-1):
        u=-1
        for v in range(1,n):
            if not added[v] and (u==-1 or min_weight[u]>min_weight[v]):
                u=v
        
        if parent[u]!=u:
            selected.append((parent[u],u))

        added[u]=True
        ret+=min_weight[u]
        
        for v,weight in adj[u].items():
            if not added[v] and min_weight[v]>weight:
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


