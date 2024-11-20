# D&C O(2^n)
def trianglepath1(y,x):
    global n,T
    if y==n-1:
        return T[y][x]
    else:
        down=trianglepath1(y+1,x)
        right=trianglepath1(y+1,x+1)
        return T[y][x]+max(down,right)

# memoization O(2^n)
def trianglepath2(y,x):
    global n,T,cache
    if y==n-1:
        return T[y][x]
    elif cache[y][x]!=-1:
        return cache[y][x]
    else:  
        down=trianglepath2(y+1,x)
        right=trianglepath2(y+1,x+1)
        cache[y][x]=T[y][x]+max(down,right)
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

# tabulation + 공간 복잡도 개선 ( 하나의 윈도우 ) : O(n^2)
def trianglepath5(n,T):
    dp=T[n-1][:]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            dp[j]=T[i][j]+max(dp[j],dp[j+1])
    return dp[0]

def trianglepath(n,T):
    path=[[0]*(i+1) for i in range(n)]
    dp=T[n-1][:]

    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if dp[j]>=dp[j+1]:
                dp[j]=T[i][j]+dp[j]
                path[i][j]-=1
            elif dp[j]<=dp[j+1]:
                dp[j]=T[i][j]+dp[j+1]
                path[i][j]+=1
                return dp[0],path

def reconstruct(y,x):
    if y==n-1:
        return T[y][x]
    elif path[y][x]==1:
        return T[y][x]+reconstruct(y+1,x+1)
    elif path[y][x]==-1:
        return T[y][x]+reconstruct(y+1,x)
    elif path[y][x]==0:
        return T[y][x]+reconstruct(y+1,x+1)


for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for _ in range(n)]
    cache=[[-1]*(i+1) for i in range(n)]
    trianglepath1(0,0)
    optval,path=trianglepath(n,T)
    optsol=reconstruct(0,0)