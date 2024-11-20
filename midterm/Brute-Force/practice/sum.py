# iteration
def sum1(n,arr):
    sum=0
    for i in range(n):
        sum+=arr[i]
    return sum

# recursion
def sum2(n,arr):
    if n==0:
        return 0
    else:
        return arr[0]+sum2(n-1,arr[1:])