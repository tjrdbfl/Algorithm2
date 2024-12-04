# Disjoin Set: 서로소 집합의 Union Find 연산
def find(a):
    if a==parent[a]:
        return a
    return find(parent[a])

def union(a,b):
    p,q=find(a),find(b)
    if p!=q:
        parent[p]=q

n=8
parent=[i for i in range(n)]
print(parent)
for i,j in [(0,2),(1,2),(3,4),(6,4),(7,4),(4,5)]:
    union(i,j)
print(parent)
union(1,4)
print(parent)

  