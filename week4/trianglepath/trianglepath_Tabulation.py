import sys

def trianglepath(n,T):
    dp=[[-1]*(i+1) for i in range(n)]
    dp[n-1]=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[i][j]=T[i][j]+max(dp[i+1,j],dp[i+1,j+1])
    return dp[0][0]

input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for i in range(n)]
    print(trianglepath(n,T))