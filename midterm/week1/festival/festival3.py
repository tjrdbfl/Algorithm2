# prefix sum  O(n^2)
def festival(N,L,cost):
    psum=cost[:]+[0]
    min_cost=float('inf')

    for i in range(N):
        psum[i]+=psum[i-1]
    
    for i in range(N):
        for j in range(i,N):
            if j-i+1>=L:
                avg_cost=(psum[j]-psum[i-1])/(j-i+1)
                min_cost=min(avg_cost,min_cost)
    
    return min_cost

# 누적합 + 범위 제한
def festival(N,L,cost):
    psum=cost[:]+[0]
    min_cost=float('inf')

    for i in range(N):
        psum[i]+=psum[i-1]
    
    for i in range(N-L+1): # 남은 길이가 L 보다 작으면 중단
        for j in range(i+L-1,N):  # 길이가 L 이상인 지점에서 시작
            if j-i+1>=L:
                avg_cost=(psum[j]-psum[i-1])/(j-i+1)
                min_cost=min(avg_cost,min_cost)
    
    return min_cost   

for _ in range(int(input())):
    N,L=map(int,input().split())
    cost=list(map(int,input().split()))
    print(festival(N,L,cost))