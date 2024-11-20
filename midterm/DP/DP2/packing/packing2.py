# packing : DP memoization
# 시간복잡도 : O(nW)

def reconstruct(i,capacity):
    if i==n:
        return []
    elif packing(i,capacity)==packing(i+1,capacity):
        return reconstruct(i+1,capacity)
    else:
        return [items[i][0]]+reconstruct(i+1,capacity-w[i])

def packing(i,capacity):
    global cache
    if i==n or capacity<=0:
        return 0
    elif cache[i][capacity]!=-1:
        return cache[i][capacity]
    else:
        pick=packing(i+1,capacity-w[i])
        drop=packing(i+1,capacity)
        cache[i][capacity]=drop if capacity < w[i] else max(drop,p[i]+pick)
        return cache[i][capacity]

for _ in range(int(input())):
    n,W=map(int,input().split())
    items=[input().split() for _  in range(n)]
    w=[int(items[i][1]) for i in range(n)] 
    p=[int(items[i][2]) for i in range(n)]
    cache=[[-1]*(W+1) for i in range(n+1)]
    optval=packing(0,W)
    optsol=reconstruct(0,W)
    print(optval,len(optsol))
    print(*optsol,sep='\n')

def reconstruct(i,capacity):
    if i==n:
        return []
    elif packing(i,capacity)==packing(i+1,capacity):
        return reconstruct(i+1,capacity)
    else:
        return [items[i][0]]+reconstruct(i+1,capacity-w[i])



