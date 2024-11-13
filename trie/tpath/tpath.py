def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return find(parent[a])

def union(a,b):
    p,q=find(a),find(b)
    if p!=q:
        parent[p]=q

def min_upperbound_kruskal(low):
    global parent,rank
    parent=list(range(n))
    rank=[1]*n
    for i in range(m):
        a,b,weight=edges[i]
        if weight>=weights[low]:
            union(a,b)
            if find(0)==find(n-1):
                return weight
    return INF

def tpath():
    global weights
    edges.sort(key=lambda x:x[2])
    weights={edges[i][2] for i in range(m)}
    weights=sorted(list(weights))
    ret=INF
    for i in range(len(weights)):
        min_upperbound=min_upperbound_kruskal(i)
        ret=min(ret,min_upperbound-weights[i])
    return ret

INF=float('inf')
for  _ in range(int(input())):
    n,m=map(int,input().split())
    edges=[list(map(int,input().split())) for _ in range(m)]
    ret=tpath()
    print(0 if ret==INF else ret)