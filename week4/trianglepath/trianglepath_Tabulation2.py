import sys

# 태뷸레이션 + 공간 복잡도 개선 
# by 슬라이딩 윈도우 (윈도우 2개 이용)
def trianglepath(n,T):
    dp=[[-1]*n for i range(2)]
    dp[(n-1)%2]=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[i%2][j]=T[i][j]+max(dp[(i+1)%2][j],dp[(i+1)%2][j+1])
    return dp[0][0]

# 태뷸레이션 + 공간 복잡도 개선 
# by 슬라이딩 윈도우 (윈도우 1개 이용)
def trianglepath2(n,T):
    dp=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j]=T[i][j]+max(dp[j],dp[j+1])
    return dp[0]

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for i in range(n)]
    print(trianglepath(n,T))
