# 이분 탐색
# O(n*logn)
from bisect import bisect_left

def lis(n,A):
    X=[A[0]] 
    for k in range(1,n):
        if X[-1]<A[k]:
            X.append(A[k])
        else: # 추가할 위치를 이분 탐색해서 k로 대체
            X[bisect_left(X,A[k])]=A[k] 
    return len(X),X

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    print(lis(n,A))
