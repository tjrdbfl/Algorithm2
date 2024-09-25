import sys

MOD=1000000007

def mmult(A,B):
    N,K,M=len(A),len(A[0]),len(B[0])
    C=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j]=(C[i][j]+(A[i][k]*B[k][j]))%MOD
    return C

def mpow(A,m):
    if m==1:
        return A
    elif m==0:
        return identity(A)
    elif m%2==1:
        return mmult(A,mpow(A,m-1))
    else:
        half=mpow(A,m//2)
        return mmult(half,half)

def tiling(n):
    if n<=2:
        return n
    else:
        A=[[1,1],[1,0]]
        return mpow(A,n)[0][0]
        
input=sys.stdin.readline
for _ in range (int(input())):
    n=int(input())
    print(tiling(n))
