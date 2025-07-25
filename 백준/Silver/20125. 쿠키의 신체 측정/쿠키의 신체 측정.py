import sys
input = sys.stdin.readline

def solution(N: list, board: list) -> None:
    left_arm = 0
    right_arm = 0
    waist = 0
    left_leg = 0
    right_leg = 0
    head = False

    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                head = (i, j)
                break
        if head:
            break

    heart = head[0] + 1
    for i in range(N):
        if board[heart][i] == '*':
            left_arm = head[1] - i
            break

    for i in range(N - 1, -1, -1):
        if board[heart][i] == '*':
            right_arm = i - head[1]
            break
    
    for i in range(N - 1, -1, -1):
        if board[i][head[1]] == '*':
            waist = i - head[0] - 1
            break

    for i in range(N - 1, -1, -1):
        if board[i][head[1] - 1] == '*':
            left_leg = i - (heart + waist)
            break
    
    for i in range(N - 1, -1, -1):
        if board[i][head[1] + 1] == '*':
            right_leg = i - (heart + waist)
            break

    print(head[0] + 2, head[1] + 1)
    print(left_arm, right_arm, waist, left_leg, right_leg)

if __name__ == "__main__":
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    solution(N, board)
