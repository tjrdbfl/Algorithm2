# Divide And Conquer
def fibonacci1(n):
    if n<=1:
        return n
    else:
        return fibonacci1(n-1)+fibonacci1(n-2)
    
# DP - Memoization
n=1
cache=[-1]*(n+1)
def fibonacci2(n):
    global cache
    if n<=1:
        return n
    elif cache[n]!=-1:
        return cache[n]
    else:
        cache[n]=fibonacci2(n-1)+fibonacci2(n-2)
        return cache[n]

# DP - Tabulation
def fibonacci3(n):
    dp=[0,1]
    for _ in range(2,n+1):
        dp.append(dp[-1],dp[-2]) # 각각 리스트의 맨 마지막 원소와 마지막에서 두 번째 원소를 의미
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
def mmult(A,B):
    assert(len(A[0]),len(B))
    C=[[-1]*M for _ in range(N)]
    N,K,M=len(A),len(A[0]),len(B)
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j]=C[i][j]+A[i][k]*B[k][j]
    return C

def identity(A):
    n=len(A)
    I=[[0]*n for _ in range(n)]
    for i in range(n):
        I[i][i]=1
    return I

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
    