import sys

def maxsum(n,A):
    curs,max=0,0
    for i in range(n):
        curs=max(curs,0)+A[i]
        maxs=max(maxs,curs)
    return maxs

input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    
    print(maxsum(N,A))