#Divide-And-Conquer
import sys

def mpow(A,m):
    if m==1:
        return A
    elif m==0:
        return identity(A)
    elif m%2==1:
        return mmult(A,mpow(A,m-1))
    else:
        half=mpow(A,m//2)
        return mmult(half,half)
    

def fsum(n):
    if n==1:
        return n
    else:
        if n%2 == 1:
            return fsum(n-1)+n
        else:    
            return 2*fsum(n//2)+n*n//4

print(fsum(int(sys.stdin.readline())))

        
