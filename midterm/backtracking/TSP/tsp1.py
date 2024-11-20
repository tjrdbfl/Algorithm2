# 완전 탐색으로 풀기(Brute-force)
# 1<<N: 10000
# (1<<N)-1:01111

def tour(path, visited, cost):
    here=path[-1]
    if visited==(1<<N)-1: # 모두 방문했으면 
        return cost+W[here][0]
    else:
        ret=INF
        for i in range(N):
            if not (visited & (1<<i)): # 방문하지 않은 정점을 시도
                path.append(i)
                ret=min(ret,tour(path,visited|(1<<i),cost+W[here][i]))
                path.pop()
        return ret

INF=float('inf')
N=int(input())
W=[list(map(int,input().split())) for _ in range(N)]
print(tour([0],1<<0,0))


