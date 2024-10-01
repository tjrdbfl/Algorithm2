import sys

def trianglepath(y,x):
    global n,T,cache
    if y==n-1:
        return T[y][x]
    elif cache[y][x]!=-1:
        return cache[y][x]
    else:
        cache[y][x]=T[y][x]+max(trianglepath(y+1,x),trianglepath(y+1,x+1))
        return cache[y][x]

input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    T=[list(map(int,input().split())) for i in range(n)]
    cache=[[-1]*(i+1) for i in range(n)]
    print(trianglepath(0,0))