# union find 개선
# 1) 경로 압축 최적화
# : find 연산을 한 번 하고 나면, 이 경로에 있는 모든 노드들은 루트를 바로 알 수 있다. 
def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a]) # 개선된 부분
    return parent[a]

# 2) 랭크에 의한 합치기
# : 트리의 높이가 높아지는 상황을 방지하기 위해
# : 두 트리를 합칠 때 항상 높이(=rank) 가 더 낮은 트리를 더 높은 트리의 서브트리로 만든다. 

def union(a,b):
    p,q=find(a),find(b)
    if p!=q:
        if rank[p]>rank[q]:
            p,q=q,p
        parent[p]=q
        if rank[p]==rank[q]:
            rank[q]+=1


n=8
parent=[2,2,3,4,5,5,4,4]
rank=[0 for _ in range(n)]
find(0)
print(parent) # [5, 2, 5, 5, 5, 5, 4, 4]
