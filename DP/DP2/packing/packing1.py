# packing : brute-force(완전 탐색, DFS)
# 시간 복잡도 :  O(2^n)
def packing(i,include):
    global optval,optsol
    if i==n: # 모든 물건을 고려했을 때 
        weight=sum[[w[j] for j in range(n) if include[j]]]
        profit=sum[[p[j] for j in range(n) if include[j]]]
        if weight<=W and optval<profit:
            optval=profit
            optsol=include[:]
    else:
        include[i]=True
        packing(i+1,include)  # i 번 물건을 담고 재취 호출
        include[i]=False
        packing(i+1,include)  # i 번 물건을 담지 않고 재귀 호출

for _ in range(int(input())):
    n,W=map(int,input().split())
    items=[input().split() for _ in range(n)]
    w=[int(items[i][1]) for i in range(n)] # 물건의 무게
    p=[int(items[i][2]) for i in range(n)] # 물건의 가치
    optval=0 # 최적값
    optsol=[]
    packing(0,[False]*n) # 0번째 item 부터 완전 탐색
    print(optval,sum(optsol))
    print(*[items[i][0] for i in range(n) if optsol[i]],sep='\n')
