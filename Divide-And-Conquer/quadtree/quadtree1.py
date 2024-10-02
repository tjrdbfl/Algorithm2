import sys

def get_next(quadtree):
    get_next.idx+=1
    return quadtree[get_next.idx-1]

def quadtree_reverse(quadtree):
    head=get_next(quadtree)
    if head in "bw":
        return head
    else:
        qt1=quadtree_reverse(quadtree)
        qt2=quadtree_reverse(quadtree)
        qt3=quadtree_reverse(quadtree)
        qt4=quadtree_reverse(quadtree)
        return "x"+qt3+qt4+qt1+qt2
        
input=sys.stdin.readline
for _ in range (int(input())):
    quadtree=input()
    get_next.idx=0 # 정적 변수로 인덱스를 초기화
    reversed=quadtree_reverse(quadtree)
    
    print(reversed)
