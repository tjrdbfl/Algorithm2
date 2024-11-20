# Matrix Multiplicaiton

# Version 1 . iteration
# assert : 조건이 true가 아닐 경우 AssertionError를 발생시키고 프로그램 멈추기
# A[0] : 행렬 A의 열 개수 (N*K)
# B : 행렬 B의 행의 개수 (K*M)
def mmult(A,B):
    assert(len(A[0])==len(B))
    N,K,M=len(A),len(A[0]),len(B[0])
    C=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for k in range(K):
                C[i][j] += A[i][k]*B[k][j]
    return C

# Recursion
C=[[0]*len(B[0]) for _ in range(len(A))]

def mmult_recur(A,B,C,i=0,j=0,k=0):
    N,K,M=len(A),len(A[0]),len(B[0])
    if i>=N:
        return C
    if j>=M:
        return mmult_recur(A,B,C,i+1,0,0)
    if k>=K:
        return mmult_recur(A,B,C,i,j+1,0)

    C[i][j]+=A[i][k]*B[k][j]

    return mmult_recur(A,B,C,i,j,k+1)