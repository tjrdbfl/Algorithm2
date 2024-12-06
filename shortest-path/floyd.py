from copy import deepcopy

def floyd(n,adj):
    D=deepcopy(adj)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j]=min(D[i][j],D[i][k]+D[k][j])

    return D

# Floyd 알고리즘
INF=float('inf')

n,m=map(int,input().split())
adj=[[INF]*n for _ in range(n)] # 인접행렬, 간선이 없으면 무한대
for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=w
for i in range(n):
    adj[i][i]=0

D=floyd(n,adj)
print("W = ",adj)
print("D = ",D)

