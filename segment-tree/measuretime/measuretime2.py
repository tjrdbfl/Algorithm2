# 병합 과정에서 역전 카운팅
# i는 왼쪽 부분 배열(A[left..mid])의 현재 위치
# j는 오른쪽 부분 배열(A[mid+1..right])의 현재 위치
def merge(A,left,mid,right):
    global inv_count
    i,j=left,mid+1
    T=[]
    while i<=mid and j<=right:
        if A[i]<=A[j]:
            T.append(A[i])
            i+=1
        else:
            T.append(A[j])
            j+=1
            inv_count+=(mid-i+1) 
    while i<=mid:
        T.append(A[i])
        i+=1
    while j<=right:
        T.append(A[j])
        j+=1
    A[left:right+1]=T[:]

def mergesort(A,left,right):
    if left==right:
        return 0 # 길이가 1인 경우 역전이 없다.
    else:
        mid=(left+right)//2
        mergesort(A,left,mid)
        mergesort(A,mid+1,right)
        merge(A,left,mid,right)

def measuretime(n,A):
    global inv_count
    inv_count=0
    mergesort(A,0,n-1)
    return inv_count

import sys

input=sys.stdin.readline
TREE_SIZE=1000000
for _ in range(int(input().strip())):
    n=int(input().strip())
    A=list(map(int,input().split()))
    measuretime(n,A)
