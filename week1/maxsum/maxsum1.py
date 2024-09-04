import sys

def festival1(N,L,cost):
    psum=cost[:]+[0]
    for i in range(N):
        psum[i]+=psum[i-1]

    min_cost=float('inf')
    for i in range(N):
        for j in range(i,N):
            if j-i+1>=L:
                avg_cost=(psum[j]-psum[i-1])/(j-i+1)
                min_cost=min(avg_cost, min_cost)
    
    return min_cost

input=sys.stdin.readline
for _ in range(int(input())):
    N,L=map(int,input().split())

    cost=list(map(int,input().split()))

    print(festival1(N,L,cost))