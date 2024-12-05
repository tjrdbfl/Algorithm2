def dfs(here,adj,seen,order):
    seen[here]=True
    for there in range(26):
        if not seen[there] and adj[here][there]:
            dfs(there,adj,seen,order)
    order.append(here)
    
# 위상 정렬 (의존성이 있는 작업들이 주어질 때, vertex를 어떤 순서로 수행해야 할지 정렬함)
# 그래프에 사이클이 있으면 None을 반환한다.
def topological_sort(adj):
    seen=[False]*26
    order=[]
    for i in range(26):
        if not seen[i]:
            dfs(i,adj,seen,order)
    order.reverse()

    for i in range(26):
        for j in range(i+1,26):
            if adj[order[j]][order[i]]:
                return None
    return order
   

# 고대어 사전 문제의 그래프 생성 (의존성을 정리한 그래프 생성)
def make_graph(word):
    adj=[[0]*26 for _ in range(26)]
    for i in range(n-1):
        for x,y in zip(word[i],word[i+1]):
            if x!=y:
                adj[ord(x)-ord('a')][ord(y)-ord('a')]=1

    return adj

for _ in range(int(input())):
    n=int(input()) # 단어 개수
    word=[input() for _ in range(n)]
    adj=make_graph(word)    # 그래프의 인접행렬
    order=topological_sort(adj) # 위상정렬
    if not order: # 사이클이 있는 경우
        print("INVALID HYPOTHESIS")
    else:
        print("".join([chr(i+ord('a')) for i in order]))