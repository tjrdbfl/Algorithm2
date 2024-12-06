def bellman_ford(src,n,adj):
    upper=[INF]*n
    upper[src]=0

    for _ in range(n):
        updated=False
        for here in range(n):
            for there,weight in adj[here].items():
                if upper[there]>upper[here]+weight:
                    upper[there]=upper[here]+weight
                    updated=True # 완화에 성공 

        if updated==False: # 모든 간선에 대해 완화가 실패했다. 
            break

    # n번째 순회에서도 완화가 성공했다면 응수 사이클이 존재한다. 
    if updated:
        return None

    return upper



# 벨만-포드 알고리즘 구현
INF=float('inf')
n,m=map(int,input().split())
adj=[{} for _ in range(n)] # [{1: 2, 2: 4}, {2: 1, 3: 7}, {3: 5}, {}]
for _ in range(m):
    u,v,w=map(int,input().split())
    adj[u][v]=w

dist=bellman_ford(0,n,adj)
print(dist)