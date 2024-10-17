# skip 추가 

length=[1] # n번째 세대의 문자열 길이를 저장

def curve(dragon,n,skip): # skip번째에 해당하는 하나의 문자를 반환 ( X, Y, F, +, -과 같은 기호 중 하나)
    if n==0:
        return dragon
    else:
        for c in dragon:
            if c in "XY":
                if skip>=length[n]:
                    skip-=length[n]
                elif c=="X":
                    return curve("X+YF",n-1,skip)
                elif c=='Y':
                    return curve("FX-Y",n-1,skip)
            elif skip>0: # F,+,- 이고 skip 이 남으면
                skip-=1
            elif skip==0: # 건너뛸 문자가 없으면 
                return c

# 추가되는 두 글자(중간에 들어가는 +YF 또는 FX-) 때문에 길이가 +2씩 더해진다.
for _ in range(50):
    length.append(2*length[-1]+2)
for _ in range(int(input())):
    n,p,L=map(int,input().split())
    dragon=""
    for i in range(L):
        skip=p-1+i
        dragon+=curve("FX",n,skip)
    print(dragon)