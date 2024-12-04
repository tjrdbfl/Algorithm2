INF=10000000000000000000
def dijkstra(src):
    global n,graph
    dist=[INF]*n
    dist[src]=1
    visited=[False]*n
    for _ in range(n):
        mindist,here=INF,-1
        for v in range(n):
            if not visited[v] and dist[v]<mindist:
                mindist,here=dist[v],v
        visited[here]=True
        for there,weight in graph[here].items():
            dist[there]=min(dist[there],dist[here]*weight)
    return dist

for _ in range(int(input())):
    n,m=map(int,input().split())
    graph={i:{} for i in range(n)}
    for _ in range(m):
        a,b,c=input().split()
        a,b,c=int(a),int(b),float(c)
        graph[a][b]=c
        graph[b][a]=c
    dist=dijkstra(0)
    print(dist[n-1])
