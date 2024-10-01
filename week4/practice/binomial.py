# 이항 계수 D&c 버전
def bino(n,k):
    if n==k or k==0:
        return 1
    else:
        return bino(n-1,k-1)+bino(n-1,k)

# 이항 계수 DP 버전(memoization)
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
                dp[i][j]=bino3(i-1,j-1)+bino3(i-1,j)
    return dp[n][k]