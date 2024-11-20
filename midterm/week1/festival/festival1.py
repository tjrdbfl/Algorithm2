# 일반적인 풀이 O(n^3)
def festival(N,L,cost):
    min_cost=float('inf')

    for i in range(N):
        for j in range(i,N):
            if j-i+1>=L:
                avg_cost=sum(cost[i:j+1])/(j-i+1)
                min_cost=min(min_cost,avg_cost)
    return min_cost
    
for _ in range(int(input())):
    N,L=map(int,input().split())
    cost=list(map(int,input().split()))
    print(festival(N,L,cost))

