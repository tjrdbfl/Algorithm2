# 삼각형 위의 최대 경로 문제 : 최적값 x, 최적해?
# 최적값(optimal value) : 경로에 포함된 숫자의 합 중에서 최댓값
# 최적해(optimal solution) : 최적값을 가지는 경로
# path[y][x]= +1 (오른쪽), -1 (아래), 0 (양쪽 다 가능)

# 경로 테이블을 이용하여 최적해를 재구성한다.
def reconstruct(y,x):
    if y==n-1: # 맨 아래 쪽에 도착한다
        return [T[y][x]]
    elif path[y][x]==-1: # 바로 아래로 내려갈 경우
        return [T[y][x]]+reconstruct(y+1,x)
    elif path[y][x]==+1: # 오른쪽 아래로 내려갈 경우
        return [T[y][x]]+reconstruct(y+1,x+1)
    else: # 어느 쪽이든 상관없다
        return [T[y][x]]+reconstruct(y+1,x+1)

# 최적해를 재구성할 수 있도록 path 테이블에 선택 경로 저장
def trianglepath(n,T):
    dp=T[n-1][:]
    path=[[0]*(i+1) for i in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            if dp[j]>=dp[j+1]: # 바로 아래가 더 크면
                dp[j]=T[i][j]+dp[j]
                path[i][j]-=1
            if dp[j]<=dp[j+1]: # 바로 오른쪽 아래 가 더 크면
                dp[j]=T[i][j]+dp[j+1]
                path[i][j]+=1
            # 둘 다 같을 경우 -1,+1 이 되므로 0이 저장됨
    return dp[0],path


for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for _ in range(n)]
    optval,path=trianglepath(n,T)
    optsol=reconstruct(0,0)
    print(optval)
    print(*optsol)
