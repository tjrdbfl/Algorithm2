def find(u):
    if u==parent[u]:
        return u
    parent[u]=find(parent[u])
    return parent[u]

def union(u,v):
    p,q=find(u),find(v)
    if p!=q:
        if rank[p]>rank[q]:
            p,q=p,q
        parent[p]=q
        if rank[p]==rank[q]:
            rank[q]+=1


def kruskal(edges):
    global parent,rank
    ret=0
    parent=list[range(n)]
    selected=[]
    rank=[1]*n
    for i in range(m):
        u,v,w=edges[i]
        if find[u]!=find[v]:
            union(u,v)
            selected.append((u,v,w))
            ret+=w
        if len(selected)==n-1:
            break
    return ret,selected

n,m=map(int,input().split())
edges=[[*map(int,input().split())]for _ in range(m)]
edges.sort(key=lambda x:x[2])
minimum,selected=kruskal(edges)