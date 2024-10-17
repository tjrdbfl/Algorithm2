# DP - tabulation + 최적해
# O(n^2)
def reconstruct(start):
    if start==-1:
        return []
    else:
        return [A[start]]+reconstruct(choices[start])

def lis(n,A):
    dp=[1]*n
    choices=[-1]*n
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if A[i]<A[j]:
                if dp[i]<dp[j]+1: # A[j]를 포함했을 때 더 긴 수열이 가능하다는 것을 의미
                    dp[i]=dp[j]+1
                    choices[i]=j # 다음 선택의 인덱스 저장
    # dp 배열에서 가장 큰 값이 있는 인덱스 찾기 (LIS의 길이를 나타내는 최대값)
    max_val = max(dp)
    # dp에서 최장 수열의 시작 위치를 찾아야 하므로 dp 값이 최대인 첫 번째 인덱스에서 시작
    start_idx = dp.index(max_val)
    
    return max_val, choices, start_idx


for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    optval, choices, start_idx = lis(n, A)
    optsol = reconstruct(start_idx)
    print(optval)
    print(*optsol)
