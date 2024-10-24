# 여행 짐싸기 문제를 백트래킹으로 해결하기

# 한계 이익 : 앞으로 더 얻을 수 있는 기대 이익 (greedy approach)
def bound(i,weight, profit):
    totweight=weight
    bound=profit
    j=i+1
    while j<n and totweight+w[j]<=W:
        totweight+=w[j]
        bound+=p[j]
        j+=1
    if j<n:
        bound+=(W-totweight)*(p[j]/w[j])
    return bound

def promising(i,weight, profit):
    global maxprofit
    if weight>=W: # 현재 무게가 배낭 용량을 초과했거나, 배낭이 이미 꽉 찬 경우
        return False
    if bound(i,weight,profit)<=maxprofit:
        return False
    return True

def search(i,weight, profit):
    global maxprofit,best,include
    if weight<=W and profit>maxprofit:
        maxprofit=profit
        best=include[:]
    if promising(i,weight,profit): # 유망한 경우 탐색, 아니면 가지치기
        include[i+1]=True
        search(i+1,weight+w[i+1],profit+p[i+1])
        include[i+1]=False
        search(i+1,weight,profit)

def packing(n,W,w,p):
    global items, maxprofit, include
    maxprofit=0
    include=[False]*n
    search(-1,0,0) # SST의 root 를 -1 로 둔다.
    return maxprofit,[items[i][0] for i in range(n) if best[i]]

for _ in range(int(input())):
    n,W=map(int, input().split())
    items=[input().split() for _ in range(n)]
    
    # 단위 무게 당 이익의 내림차순으로 아이템을 정렬
    items.sort(key=lambda x: int(x[2])/int(x[1]),reverse=True)
    w=[int(items[i][1]) for i in range(n)]
    p=[int(items[i][2]) for i in range(n)]
    optval, optsol=packing(n,W,w,p)
    print(optval,len(optsol))
    print(*optsol,sep='\n')
