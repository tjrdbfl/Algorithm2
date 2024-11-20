# 이항 계수 D&C 버전
def bino(n,k):
    if n==k or k==0:
        return 1
    else:
        return bino(n-1,k-1)+bino(n-1,k)

# 이항 계수 DP 버전(memoization)
# **nCk**를 계산하기 위해서는 0 ≤ k ≤ n 범위의 값들을 모두 다룰 수 있어야 하기 때문
n=10
cache=[[-1]*(i+1) for i in range(n+1)]

def bino2(n,k):
    global cache #캐시는 주로 전역 변수로 선언
    if n==k or k==0:
        return 1
    elif cache[n][k]!=-1: #이미 계산된 결과가 있으면
        return cache[n][k] #기존에 계산한 값 재활용
    else:
        cache[n][k]=bino2(n-1,k-1)+bino2(n-1,k)
        return cache[n][k]

# 이항 계수 DP 버전(tabulation)
def bino3(n,k):
    dp=[[-1] * (i+1) for i in range(n+1)] # DP 테이블을 구성하고 상향식으로 계산
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==i or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return dp[n][k]


# 이항 계수 DP 버전(tabulation) + 공간 복잡도 개선 ( 1개의 슬라이딩 윈도우 )
def bino4(n,k):
    dp=[0]*(k+1)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(min(i,k),0,-1):
            dp[j]=dp[j]+dp[j-1]
    return dp[k]

