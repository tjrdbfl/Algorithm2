# 게임판 덮기
from itertools import product

# 주어직 칸을 덮을 수 있는 4가지 방법
# 블록을 구성하는 3칸의 상대적 위치. 기준점(0,0)
# dy,dx
coverType = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]

# 아직 채우지 못한 칸 중 가장 윗줄 가장 왼쪽에 있는 칸을 찾는다.
def find_white(board,H,W):
    for i,j in product(range(H),range(W)):
        if board[i][j]==0:
            return i,j
    return -1,-1

# delta가 1이면 덮고, delta가 -1이면 덮었던 블록을 제거
def place(board,y,x,type,delta,H,W):
    ok=True
    for i in range(3):
        ny=y+coverType[type][i][0]
        nx=x+coverType[type][i][1]
        if not ((0<=ny<H) and (0<=nx<W)): # 보드 밖으로 나간 경우
            ok=False
        else:
            board[ny][nx]+=delta
            if(board[ny][nx]>1): # 검은 칸이거나 겹쳐서 덮는 경우
                ok=False
    return ok
         
# board의 모든 빈 칸을 덮을 수 있는 방법의 수 반환
def cover(H,W,board):
    y,x=find_white(board,H,W)
    if y==-1:
        return 1
    else:
        ret=0
        for type in range(4): # 모든 블록 유형에 대해 덮어보기
            if place(board,y,x,type,1,H,W): # 만약 덮을 수 있으면 재귀호출
                ret+=cover(H,W,board) 
            place(board,y,x,type,-1,H,W) # 덮은 블록을 제거한다
        return ret


# 입력 '#'(1) 과 '.' 을 각각 1과 0으로 바꿔
# product(range(H),range(W)) :H=2, W=3일 때, product(range(2), range(3))는 (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)
# board[i][j]=='#' -> 1 
# board[i][j]==0 (빈칸)
def boardcover(H,W,board):
    board2=[[0]*W for _ in range(H)]
    for i,j in product(range(H),range(W)):
        board2[i][j]=[0,1][board[i][j]=='#']
    if sum([row.count(0) for row in board2])%3!=0:
        return 0
    else:
        return cover(H,W,board2)


for _ in range(int(input())):
    H,W=map(int,input().split())
    board=[input() for _ in range(H)]
    print(boardcover(H,W,board))