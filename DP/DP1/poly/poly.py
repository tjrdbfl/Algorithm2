MOD = 10000000

# D&C
def poly(n,first):
    if n==first:
        return 1
    else:
        ret=0
        for second in range(1,n-first+1):
            ret=(ret+(first+second-1)*(poly(n-first,second)))%MOD
        return ret

# Memoization
def poly1(n,first):
    global cache
    if n==first:
        return 1
    elif cache[n][first]!=-1:
        return cache[n][first]
    else:
        ret=0
        for second in range(1,n-first+1):
            ret=(ret+(first+second-1)*poly1(n-first,second))%MOD
        cache[n][first]=ret
        return cache[n][first]

# Tabulation
def poly2(n,first):
    dp=[[0]*(i+1) for i in range(n+1)]
    for i in range(1,n+1):
        for first in range(1,i+1):
            if i==first:
                dp[i][first]=1
            else:
                ret=0
                for second in (1,i-first+1):
                    ret=(ret+(first+second-1)*dp[i-first][second])%MOD
                dp[i][first]=ret
    return sum(dp[n])%MOD      

# 입력
for _ in range(int(input())):
    n=int(input())
    ret=0
    cache=[[-1]*(i+1) for i in range(n+1)]
    for first in range(1,n+1):
        ret=(ret+poly(n,first))%MOD
    print(ret)
