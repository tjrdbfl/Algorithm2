from heapq import heappush,heappop
# Dijkstra 알고리즘 구현
def dijkstra2(src,n,adj):
    dist=[INF]*n
    dist[src]=0
    pq=[]
    heappush(pq,(dist[src],src))

    while pq:
        dist,here=heappop(pq)
        
        for there,weight in adj[here].items():
            if dist[there]>dist[here]+weight:
                dist[there]=dist[here]+weight
                heappush(pq,(dist[there],there))

    return dist

def dijkstra(src):
    dist=[INF]*n
    seen=[False]*n
    dist[src]=0
    seen[src]=True

    for _ in range(n):
        closest,here=INF,-1
        for i in range(n):
            if not seen[i] and dist[i]<closest:
                closest,here=dist,i

        if closest==INF:
            break
        
        seen[here]=True

        for there,weight in adj[here].items():
            if not seen[there]:
                dist[there]=min(dist[there],dist[here]+weight)

    return dist


INF=float('inf')
n,m=map(int,input().split())
adj=[{} for _ in range(n)] # [{1: 2, 2: 4}, {2: 1, 3: 7}, {3: 5}, {}]
for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=w

dist=dijkstra(0)
print(dist)