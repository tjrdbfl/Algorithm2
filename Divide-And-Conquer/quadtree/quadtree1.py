# 압축 해제(decompress) & 압축(compress)

import sys

def get_next(quadtree):
    get_next.idx+=1
    return quadtree[get_next.idx-1]

def decompress(quadtree,y,x,size,decompressed):
    head=get_next(quadtree)
    if head in "bw":
        for i in range(y, y+size):
            decompressed[i][x:x+size]=[(head=="b")*1]*size
    else:
        half=size//2
        decompress(quadtree,y,x,half,decompressed)
        decompress(quadtree,y,x+half,half,decompressed)
        decompress(quadtree,y+half,x,half,decompressed)
        decompress(quadtree,y+half,x+half,half,decompressed)

def check(decompressed,y,x,size):
    s=sum([sum(decompressed[i][x:x+size]) for i in range(y,y+size)])
    return "w" if s==0 else "b" if s==size*size else "x"

def compress(decompressed,y,x,size):
    head=check(decompressed,y,x,size)
    if head!="x":
        return head
    else:
        half=size//2
        q1=compress(decompressed,y,x,half)    
        q2=compress(decompressed,y,x+half,half)
        q3=compress(decompressed,y+half,x,half)
        q4=compress(decompressed,y+half,x+half,half)
        return "x"+q1+q2+q3+q4

# get_next.idx=0 # 정적 변수로 인덱스를 초기화 해준 이유?
# 정적 변수 사용할 경우, 다음 호출 시에도 증가된 상태로 사용 가능
# 정적 변수 사용하지 않을 경우, 인덱스가 다시 0으로 초기화됨

input=sys.stdin.readline
for _ in range(int(input())):
    quadtree=input()
    size=len(quadtree)
    get_next.idx=0
    decompressed=[[0]*size for _ in range(size)] 
    decompress(quadtree,0,0,size,decompressed)
    print()
    for i in range(len(decompressed)):
        print(*decompressed[i])
    print(compress(decompressed,0,0,size))