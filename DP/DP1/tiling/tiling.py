MOD=1000000007

def mmult(A,B):
    assert(len(A[0]),len(B))
    C=[[-1]*M for _ in range(N)]
    N,K,M=len(A),len(A[0]),len(B)
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j]=(C[i][j]+A[i][k]*B[k][j])%MOD
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
    
def tiling(n):
    if n<=2:
        return n
    else:
        A=[[1,1],[1,0]]
        return mpow(A,n)[0][0]
     
for _ in range(int(input())):
    n=int(input())
    print(tiling(n))