# D&C
def trianglepath1(y,x):
    global n,T
    if y==n-1:
        return T[y][x]
    else:
        down=trianglepath1(y+1,x)
        right=trianglepath1(y+1,x+1)
        return T[y][x]+max(down,right)

# memoization
def trianglepath2(y,x):
    global n,T,cache
    if y==n-1:
        return T[y][x]
    elif cache[y][x]!=-1:
        return cache[y][x]
    else:
        down=trianglepath2(y+1,x)
        right=trianglepath2(y+1,x+1)
        cache[y][x]=cache[y][x]+max(down,right)
        return cache[y][x]

# tabulation 1
def trianglepath3(n,T):
    dp=[[-1]*(i+1) for i in range(n)]
    dp[n-1]=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[i][j]=T[i][j]+max(dp[i+1][j],dp[i+1][j+1])
    return dp[0][0]

# tabulation + 공간 복잡도 개선 ( 2개의 윈도우 )
def trianglepath4(n,T):
    dp=[[-1]*n for _ in range(2)]
    dp[(n-1)%2]=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[i%2][j]=T[i][j]+max(dp[(i+1)%2][j],dp[(i+1)%2][j+1])
    return dp[0][0]

# tabulation + 공간 복잡도 개선 ( 하나의 윈도우 )
def trianglepath5(n,T):
    dp=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j]=T[i][j]+max(dp[j],dp[j+1])
    return dp[0]


for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for _ in range(n)]
    cache=[[-1]*(i+1) for i in range(n)]
    trianglepath1(0,0)