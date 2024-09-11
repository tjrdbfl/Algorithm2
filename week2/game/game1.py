import sys
from itertools import product

coverType = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]


def find_white(H, W, board):
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def place(board, y, x, type, delta, H, W):
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if not ((0 <= ny < H) and (0 <= nx < W)):
            ok = False
        else:
            board[ny][nx] += delta
            if board[ny][nx] > 1:
                ok = False
    return ok


def cover(H, W, board):
    y, x = find_white(H, W, board)
    if y == -1:
        return 1
    else:
        ret = 0
        for type in range(4):
            if place(board, y, x, type, 1, H, W):
                ret += cover(H, W, board)
            place(board, y, x, type, -1, H, W)  # 되돌리기
        return ret


def boardcover(H, W, board):
    board2 = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            board2[i][j] = 0 if board[i][j] == '.' else 1
    if sum(row.count(0) for row in board2) % 3 != 0:
        return 0
    else:
        return cover(H, W, board2)


input = sys.stdin.readline
for _ in range(int(input())):
    H, W = map(int, input().split())
    board = [input().rstrip() for _ in range(H)]  # 개행 문자 제거
    print(boardcover(H, W, board))