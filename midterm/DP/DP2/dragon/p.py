length=[1]
def curve(dragon,n,skip):
    if n==0:
        return dragon
    else:
        for c in dragon:
            if c in "XY":
                if skip>=length[n]:
                    skip-=length[n]
                elif dragon in "X":
                        return("X+YF",n-1,skip)
                elif dragon in "Y":
                    return curve("FX-Y",n-1,skip)        
            else:
                if skip>0:
                    skip+=1
                if skip==0:
                    return c


for i in range(50):
    length.append(length[-1]*2+2)
for _ in range(int(input())):
    n,p,L=map(int,input().split())
    dragon=""
    for i in range(L):
        dragon+=curve("XY",n,p-1+i)
    print(dragon)

