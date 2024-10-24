# 유망 함수 있는 버전
def rotate(block):
    return list(zip(*reversed(block)))

def generated_rotation(block):
    rotations=[[] for _ in range(4)]
    for rot in range(4):
        originY=originX=-1
        for i in range(len(block)):
            for j in range(len(block[0])):
                if block[i][j]==1:
                    if originY==-1:
                        originY,originX=i,j
                    rotations[rot].append((i-originY,j-originX))

        block=rotate(block)

    blocks={tuple(block) for block in rotations}
    return list(blocks)

def find_white(H,W,board):
    for i in range(H):
        for j in range(W):
            if board[i][j]==0:
                return i,j
    return -1,-1

def place(y,x,block,delta):
    global board
    ok=True
    for i in range(len(block)):
        ny=y+block[i][0]
        nx=x+block[i][1]

        if not ((0<=ny<H) and (0<=nx<W)):
            ok=False
        else:
            board[ny][nx]+=delta
            if board[ny][nx]>1:
                ok=False
    return ok

def search(placed, blanks):
    global best
    if placed+(blanks//block_size) <= best: # 유망함수
        return
    y,x=find_white(H,W,board)
    if y==-1:
        best=max(best,placed)
    else:
        for i in range(len(rotations)):
            if place(y,x,rotations[i],1):
                search(placed+1,blanks-block_size)
            place(y,x,rotations[i],-1)
        
        board[y][x]=1
        search(placed,blanks-1)
        board[y][x]=0

for _ in range(int(input())):
    H,W,R,C=map(int,input().split())
    board=[[[0,1][x=='#'] for x in input()] for _ in range(H)]
    block=[[[0,1][x=='#'] for x in input()] for _ in range(R)]
    rotations=generated_rotation(block)
    block_size=len(rotations[0])
    blanks=sum([board[i].count(0) for i in range(H)])
    best=0
    search(0,blanks)
    print(best)
