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
