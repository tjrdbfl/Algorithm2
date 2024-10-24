# DFS (유망 함수 없는 버전)
# 블록의 회전에 따른 4개의 형태, 블록에 대한 전처리 필요
# 유망 함수 없는 버전
def rotate(block):
    return list(zip(*reversed(block)))

# block 의 4가지 회전 형태를 만들고, 상대 좌표를 리스트로 반환 
def generate_rotations(block):
    rotations=[[] for _ in range(4)]
    for rot in range(4): # 모든 회전 형태에 대해서
        originX=originY=-1 # 원점 초기화
        for i in range(len(block)):
            for j in range(len(block[0])):
                if block[i][j]==1:
                    if originY==-1: # 가장 맨 윗쪽에 있는 칸이 원점
                        originY,originX=i,j
                    rotations[rot].append((i-originY,j-originX))
        
        block=rotate(block)

    # block 의 회전 형태 중 중복이 있을 경우(상하/좌우) 중복을 제거    
    blocks={tuple(block) for block in rotations}
    return list(blocks)

def find_white(board,H,W):
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
        if not ((0<=ny<H) and (0<=nx<W)):  # 검은 칸이거나 겹쳐서 덮는 경우
            ok=False
        else:
            board[ny][nx]+=delta
            if (board[ny][nx]>1):
                ok=False
    return ok

# placed: 지금까지 높인 블록의 수
def search(placed): 
    global best
    y,x=find_white(board,H,W) # 비어 있는 가장 왼쪽 칸 찾기
    if y==-1: # 게임 판의 모든 칸을 처리
        best=max(best,placed) # 최적 값 업데이트
    else:
        for i in range(len(rotations)):
            if place(y,x,rotations[i],1): # 이 칸을 덮었다면
                search(placed+1)
            place(y,x,rotations[i],-1)
        
        board[y][x]=1 # 이 칸을 덮지 않고 '막아' 두고
        search(placed) # placed 값을 그대로 두고 재귀 호출
        board[y][x]=0

for _ in range(int(input())):
    H,W,R,C=map(int,input().split())
    board=[[[0,1][x=='#'] for x in input()] for _ in range(H)]
    block=[[[0,1][x=='#'] for x in input()] for _ in range(R)]
    rotations=generate_rotations(block) 
    best=0
    search(0)
    print(best)
