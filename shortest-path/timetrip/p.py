# Floyd 알고리즘을 응용하여 reachable 배열 만들기
# D[i][j] = True : i 에서 j로 가는 경로가 있다. False : 없다 
def pathfind(n,reachable):
    for i in range(n):
        reachable[i][i]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachable[i][j]=reachable[i][j] or (reachable[i][k] and reachable[k][j])
    
# Bellman-Ford 알고리즘을 이용하여 시간 여행 문제 해결하기 
def timetrip(src,target,n,adj,reachable):
    upper=[INF]*n
    upper[src]=0

    for _ in range(n-1):
        for here in range(n):
            for there,weight in adj[here]:
                upper[there]=min(upper[there],upper[here]+weight)

    for here in range(n):
        for there,weight in adj[here]:
            if upper[there]>upper[here]+weight: # n 번째 완화 성공으로 음수 사이클이 들어있다. 
                if reachable[src][here] and reachable[here][target]: # 이 음수 사이클을 포함하는 경로가 있으면
                    return -INF 
    return upper[target]

INF=float('inf')
# 멀티 그래프 
for _ in range(int(input())):
    n,m=map(int,input().split())
    adj1=[[] for _ in range(n)]
    adj2=[[] for _ in range(n)]
    reachable=[[False]*n for _ in range(n)]
    
    for _ in range(m):
        a,b,d=map(int,input().split())
        adj1[a].append((b,d))
        adj2[a].append((b,-d))
        reachable[a][b]=True

    pathfind(n,reachable)

    ret1=timetrip(0,1,n,adj1,reachable)
    ret2=timetrip(0,1,n,adj2,reachable)

    if not reachable[0][1]:
        print("UNREACHABLE")
    else:
        print("INFINITY" if ret1==-INF else ret1, end=" ")
        print("INFINITY" if ret2==-INF else -ret2)