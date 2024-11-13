# DP tabulation

def packing(n,w,W,p):
    global optsol
    dp=[[0]*(W+1) for _ in range(n+1)]
    # 최적값 
    for i in range(1,n+1):
        for j in range(1,W+1):
            if w[i-1]>j: # 넣으려는 items의 무게 > 남아있는 용량 (아이템 안 넣을 때)
                dp[i][j]=dp[i-1][j]
            else: # item 넣을 때 
                dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
    
    # 최적해의 역추적
    optsol=[]
    j=W
    for i in range(n,0,-1):
        if dp[i-1][j]!=dp[i][j]: # 아이템을 넣었을 때만 
            optsol.append(i-1)
            j-=w[i-1] # i = 1일 때 첫 번째 아이템의 무게는 w[0]에 있고, i = 2일 때 두 번째 아이템의 무게는 w[1]에 있습니다.
            
    return dp[n][W]

for _ in range(int(input())):
    n,W=map(int,input().split())
    items=[input().split() for _ in range(n)]
    w=[int(items[i][1]) for i in range(n)]
    p=[int(items[i][2]) for i in range(n)]
    optval=packing(n,w,W,p)
    optsol.reverse()
    print(optval,len(optsol))
    print(*[items[i][0] for i in optsol],sep='\n')
