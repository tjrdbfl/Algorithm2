import sys

# Divde and Conquer
def trianglepath(y,x):
    global n,T
    if y==n-1:
        return T[y][x]
    else:
        return T[y][x]+max(trianglepath(y+1,x),trianglepath(y+1,x+1))

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for i in range(n)]
    return trianglepath(0,0)

