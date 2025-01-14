import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(N: int, board: list) -> None:
    answer = 0

    def move(board, d):
        new_board = [[0] * N for _ in range(N)]
        for i in range(N):
            if d == 0:
                now = 0
                index = 0
                for j in range(N):
                    if board[i][j] == 0:
                        continue
                    if now == 0:
                        now = board[i][j]
                    elif board[i][j] == now:
                        new_board[i][index] = now * 2
                        now = 0
                        index += 1
                    elif now > 0 and board[i][j] != now:
                        new_board[i][index] = now
                        now = board[i][j]
                        index += 1
                new_board[i][index] = now

            if d == 1:
                now = 0
                index = N - 1
                for j in range(N - 1, -1, -1):
                    if board[i][j] == 0:
                        continue
                    if now == 0:
                        now = board[i][j]
                    elif board[i][j] == now:
                        new_board[i][index] = now * 2
                        now = 0
                        index -= 1
                    elif now > 0 and board[i][j] != now:
                        new_board[i][index] = now
                        now = board[i][j]
                        index -= 1
                new_board[i][index] = now

            if d == 2:
                now = 0
                index = 0
                for j in range(N):
                    if board[j][i] == 0:
                        continue
                    if now == 0:
                        now = board[j][i]
                    elif board[j][i] == now:
                        new_board[index][i] = now * 2
                        now = 0
                        index += 1
                    elif now > 0 and board[j][i] != now:
                        new_board[index][i] = now
                        now = board[j][i]
                        index += 1
                new_board[index][i] = now

            if d == 3:
                now = 0
                index = N - 1
                for j in range(N - 1, -1, -1):
                    if board[j][i] == 0:
                        continue
                    if now == 0:
                        now = board[j][i]
                    elif board[j][i] == now:
                        new_board[index][i] = now * 2
                        now = 0
                        index -= 1
                    elif now > 0 and board[j][i] != now:
                        new_board[index][i] = now
                        now = board[j][i]
                        index -= 1
                new_board[index][i] = now
        return new_board
    
    def back(board, cnt):
        nonlocal answer
        if cnt == 5:
            now = 0
            for i in range(N):
                now = max(now, max(board[i]))
            answer = max(answer, now)
            return
        for i in range(4):
            new_board = move(board, i)
            back(new_board, cnt + 1)
        
    back(board, 0)
    print(answer)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
solution(N, board)
