from bisect import bisect_left

def matchorder(n,russian,korean):
    korean.sort()
    wins=0
    for i in range(n):
        if korean[-1]<russian[i]:
            korean.pop(0)
        else:
            wins+=1
            korean.pop(bisect_left(korean,russian[i]))
    return wins

for _  in range(int(input())):
    n=int(input())
    russian=list(map(int,input().split()))
    korean=list(map(int,input().split()))
    print(matchorder(n,russian,korean))