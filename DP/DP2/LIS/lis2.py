# DP - memoization
def lis(start):
    global cache
    if cache[start]!=-1:
        return cache[start]
    else:
        ret=1
        for j in range(start+1,n):
            if A[start]<A[j]:
                ret=max(ret,1+lis(j))
        cache[start]=ret
        return cache[start]

for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    cache=[-1]*n
    print(max(lis(i) for i in range(n)))


