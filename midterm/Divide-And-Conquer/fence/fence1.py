import sys

def largest_in_between(h,left,mid,right):
    low,high=mid,mid+1
    height=min(h[low],h[high])
    ret=height*2
    while left<low or right>high:
        if high<right and (low==left or h[low-1]<h[high+1]):
            high+=1
            height=min(height,h[high])
        else:
            low-=1
            height=min(height,h[low])
        ret=max(ret,height*(high-low+1))
    return ret


def fence(h,left,right):
    if left==right:
        return h[left]
    else:
        mid=(left+right)//2
        ret=max(fence(h,left,mid),fence(h,mid+1,right))
        return max(ret,largest_in_between(h,left,mid,right))

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    print(fence(h,0,n-1))