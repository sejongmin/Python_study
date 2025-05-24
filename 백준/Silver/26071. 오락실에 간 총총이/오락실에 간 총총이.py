import sys
input = sys.stdin.readline


def solution(N, board):
    answer = 0
    min_x = min_y = N - 1
    max_x = max_y = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'G':
                if min_x > j:
                    min_x = j
                if max_x < j:
                    max_x = j
                if min_y > i:
                    min_y = i
                if max_y < i:
                    max_y = i
    if min_x != max_x:
        answer += min(max_x, N - 1 - min_x) 
    if min_y != max_y:
        answer += min(max_y, N - 1 - min_y)

    return answer

N = int(input())
board = [list(input().strip()) for _ in range(N)]
print(solution(N, board))