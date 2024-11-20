# packing : DP memoization
# 공간 복잡도 개선 : 2차원 배열 대신 dictionary 사용

def reconstruct(i,capacity):
    if i==n:
        return []
    elif packing(i+1,capacity)==packing(i,capacity):
        return reconstruct(i+1,capacity)
    else:
        return [items[i][0]]+reconstruct(i+1,capacity-w[i])

def packing(i,capacity):
    global cache,optval,optsol
    if i==n or capacity<=0:
        return 0
    elif (i,capacity) in cache:
        return cache[(i,capacity)]
    else:
        pick=packing(i+1,capacity-w[i])
        drop=packing(i+1,capacity)
        cache[(i,capacity)]=drop if capacity<w[i] else max(drop,p[i]+pick)
        return cache[(i,capacity)]

for _ in range(int(input())):
    n,W=map(int,input().split())
    items=[input().split() for _ in range(n)]
    w=[int(items[i][1]) for i in range(n)]
    p=[int(items[i][2]) for i in range(n)]
    cache={}
    optval=packing(0,W)
    optsol=reconstruct(0,W)
    print(optval,len(optsol))
    print(*optsol,sep='\n')