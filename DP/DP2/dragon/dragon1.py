# 무식하게 풀기
# 드래곤 커브
# n: 세대 수
# p: p번 째부터 L개 글자 출력
def curve(dragon,n):
    if n==0:
        return dragon
    else:
        ret=""
        for c in dragon:
            if c=="X":
                ret+=curve("X+YF",n-1)
            elif c=="Y":
                ret+=curve("FX-Y",n-1)
            else: # F,+,- 이면 그대로
                ret+=c
        return ret

for _ in range(int(input())):
    n,p,L=map(int,input().split())
    dragon=curve("FX",n)
    print(dragon[p-1:p-1+L])