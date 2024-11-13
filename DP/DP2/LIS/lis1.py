# LIS (Longest Increasing Subsequence)
# DFS (완전 탐색)

def lis(n,A):
    if not A: 
        return 0
    else:
        ret=0
        for i in range(n):
            B=[] #A[i] 뒤에 있는 A[i] 보다 큰 수들의 부분 수열
            for j in range(i+1,n):
                if A[i]<A[j]:
                    B.append(A[j]) # for 문 끝

            ret=max(ret,1+lis(len(B),B))
        return ret

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    print(lis(n,A))










