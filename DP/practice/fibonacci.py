# Divide And Conquer
def fibonacci1(n):
    if n<=1:
        return n
    else
        return fibonacci1(n-1)+fibonacci1(n-2)
    
# DP - Memoization
cache=[-1]*n
def fibonacci2(n):
    global cache
    if n<=1:
        return n
    elif cache[n]!=-1
        return cache[n]
    else:
        cache[n]=fibonacci2(n-1)+fibonacci2(n-2)
        return cache[n]

# DP - Tabulation
def fibonacci3(n):
    dp=[0,1]
    for i in range(2,n+1):
        dp.append(dp[n-1],dp[n-2])
    return dp[n]
    
# DP - Tabulation + 공간 복잡도 개선
def fibonacci4(n):
    if n<=1:
        return n
    else:
        a,b=0,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b


# DP - 행렬 거듭 제곱이용
def mpow(A,n):
    if n==1:
        return A
    elif n==0:
        return identity(A)
    elif n%2==1:
        return mmult(A,mpow(A,n-1))
    else:
        half=mpow(A,n//2)   # n//2 => n 을 2로 나눈 몫
        return mmult(half,half)

def fibonacci5(n):
    if n<=1:
        return n
    else:
        A=[[1,1],[1,0]]
        return mpow(A,n-1)[0][0]