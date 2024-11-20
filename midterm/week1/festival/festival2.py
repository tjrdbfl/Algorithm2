# 슬라이딩 윈도우  O(n^2)
def festival(N,L,cost):
    min_cost=float('inf')

    for i in range(N):
        tot_cost=0
        for j in range(i,N):
            tot_cost+=cost[i]
            if j-i+1>=L:
                avg_cost=tot_cost/(j-i+1)
                min_cost=min(min_cost,avg_cost)

    return min_cost

for _ in range(int(input())):
    N,L=map(int,input().split())
    cost=list(map(int,input().split()))
    print(festival(N,L,cost))