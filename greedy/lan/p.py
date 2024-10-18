# LAN with Prim's Algorithm
import math

def lan(n,W):
    # 출발 정점은 0번 정점
    dist=[W[0][i] for i in range(n)]
    ret=0

    # n-1 개의 정점만 검사해도 다 검사 가능
    for _ in range(n-1):
        min=float('inf')
        # 현재 MST에 추가되지 않은 정점들 중에서 가장 가까운 정점인 vnear를 찾기
        for u in range(1,n): # 0 정점을 제외하고 
            if 0<=dist[u]<min:
                min=dist[u]
                vnear=u

        # 찾은 정점을 방문한다
        # sqrt(16) = 4
        # dist[vnear] = -1는 Prim's 알고리즘에서 **해당 정점(vnear)**이 이미 방문되었음을 표시하는 역할
        ret+=math.sqrt(dist[vnear])
        dist[vnear]=-1

        # MST에 포함되지 않은 다른 정점들과의 거리를 업데이트하는 역할
        for u in range(1,n):
            if dist[u]>W[u][vnear]:
                dist[u]=W[u][vnear]

    return ret


for _ in range(int(input())):
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    W=[[0]*n for _ in range(n)] # 인접 행렬

    # 가중치 행렬 만들기
    for u in range(n):
        for v in range(n):
            W[u][v]=W[v][u]=(x[u]-x[v])**2+(y[u]-y[v])**2

    for _ in range(m):
        u,v=map(int,input().split())
        W[u][v]=W[v][u]=0 # 이미 설치된 케이블의 가중치를 0으로 설정한다. 
    
    print(f"{lan(n,W):08f}")

def lan(n,W): 
    ret=0
    dist=[W[0][i] for i in range(n)]

    for _ in range(n-1):
        min=float('inf')
        for i in range(1,n):
            if 0<=dist[i]<min:
                min=dist[i]
                vnear=i
        
        ret+=math.sqrt(dist[vnear])
        dist[i]=-1

        for i in range(1,n):
            if dist[i]>W[i][vnear]:
                dist[i]=W[i][vnear]

    return ret