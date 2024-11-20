def rcomb(n, comb=[],start=0):
    if len(comb)==4:
        print(*comb)
    else:
        for i in range(start,n):
            rcomb(n,comb+[i],i+1)

def sumi(n,arr):
    if n==0:
        return 0
    else:
        sum=0
        for i in range(n):
            sum+=arr[i]
        return sum
    
def sumr(n,arr):
    if n==0:
        return 0
    else:
        return arr[0]+sumr(n-1,arr[1:])