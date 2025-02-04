import sys
input = sys.stdin.readline

def solution(board, zeros):
    def check_row(r, num):
        for i in range(9):
            if num == board[r][i]:
                return False
        return True
    
    def check_col(c, num):
        for i in range(9):
            if num == board[i][c]:
                return False
        return True
    
    def check_block(r, c, num):
        r = r // 3 * 3
        c = c // 3 * 3
        for i in range(3):
            for j in range(3):
                if num == board[r+i][c+j]:
                    return False
        return True

    def back(depth):
        if depth == len(zeros):
            for i in range(9):
                print(*board[i], sep="")
            exit()

        r, c = zeros[depth]
        for num in range(1, 10):
            if check_row(r, num) and check_col(c, num) and check_block(r, c, num):
                board[r][c] = num
                back(depth + 1)
                board[r][c] = 0

    back(0)

board = []
zeros = []
for i in range(9):
    line = list(map(int, input().strip()))
    for j in range(9):
        if line[j] == 0:
            zeros.append((i, j))
    board.append(line)
solution(board, zeros)
