# LIS 중 사전 순서대로 맨 앞에서 k번째 있는 LIS를 출력하는 프로그램
# 사전 순서대로 : 숫자가 작은 것부터 차례로 나열하는 순서
MAX=2000000001

# S[start]에서 시작하는 LIS 중 사전순으로 skip 개 건너뛴 수열을 result에 저장
def reconstruct(start,skip,result):
    result.append(A[start])
    followers=[] # 뒤에 오는 숫자들의 위치와 목록
    for next in range(start+1,n):
        if (start==-1 or A[start]<A[next]) and dp_len[start]==dp_len[next]+1:
            followers.append((A[next],next))
    followers.sort() # 오름차순 정렬
    for f in followers:
        cnt=dp_cnt[f[1]]
        if cnt<=skip:
            skip-=cnt
        else:
            reconstruct(f[1],skip,result)
            break


# LIS의 길이를 저장하는 DP 테이블 생성
def make_length(n,A):
    dp=[1]*(n+1) # -inf를 추가했으므로 크기는 n+1
    for i in range(n-1,-2,-1):
        for j in range(i+1,n):
            if A[i]<A[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp

# LIS의 개수를 저장하는 DP 테이블 생성
def make_count(n,A):
    dp=[1]*(n+1)    # -inf를 추가했으므로 크기는 n+1
    for i in range(n-1,-2,-1):
        if dp_len[i]==1:
            dp[i]=1
        else:
            ret=0
            for j in range(i+1,n):
                if A[i]<A[j] and dp_len[i]==dp_len[j]+1: # LIS의 길이를 정확하게 유지하면서 i 번째 원소를 포함하는 LIS를 만드는 경우만 고려하겠다는 의미
                    ret=min(MAX,ret+dp[j]) # LIS 의 개수가 최악의 경우 매우 커질 수 있어서 이를 방지하기 위해 
            dp[i]=ret
    return dp

def klis(n,k,A):
    global dp_len,dp_cnt 
    A+=[-float('inf')]  # 마지막에 -inf 추가
    dp_len=make_length(n,A)
    dp_cnt=make_count(n,A)
    optsol=[]
    reconstruct(-1,k-1,optsol) # index가 0부터 시작해서 k 번째를 구하려면 k-1 index를 구해야 함함
    print(dp_len[-1]-1) # -inf 의 LIS에서 1을 뺀 값이 최적값
    print(*optsol[1:]) # 최적해에서 -inf 를 제외하고 출력

for _ in range(int(input())):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    klis(n,k,A)

# dp_len : 각 위치에서 시작하는 LIS (Longest Increasing Subsequence, 최장 증가 부분 수열)의 길이를 저장하는 DP 테이블



 