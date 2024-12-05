# adjacent metrix
n,m=map(int,input().split())
adjacent=[[0]*n for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    adjacent[u][v]=1

print(adjacent)

# adjacent list
n,m=map(int,input().split())
adjlist={i:[] for i in range(n)}
for _ in range(m):  
    u,v=map(int,input().split())
    adjlist[u].append(v)

print(adjlist)
