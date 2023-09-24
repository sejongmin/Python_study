def UPDATE(board, merge, order):
    _, r, c, value = order
    r, c = int(r), int(c)
    
    board[r - 1][c - 1] = value
    for i, j in merge[r - 1][c - 1]:
        board[i - 1][j - 1] = value
    
def UPDATEALL(board, order):
    _, value1, value2 = order
    for i in range(50):
        for j in range(50):
            if board[i][j] == value1:
                board[i][j] = value2
                
def MERGE(board, merge, order):
    _, r1, c1, r2, c2 = order
    r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)

    for val in merge[r2 - 1][c2 - 1]:
        merge[r1 - 1][c1 - 1].append(val)
            
    for val in merge[r1 - 1][c1 - 1]:
        merge[r2 - 1][c2 - 1].append(val)
            
    for i, j in merge[r1 - 1][c1 - 1]:
        merge[i - 1][j - 1].append([r2, c2])
        if merge[r2 - 1][c2 - 1]:
            for val in merge[r2 - 1][c2 - 1]:
                merge[i - 1][j - 1].append(val)
    merge[r1 - 1][c1 - 1].append([r2, c2])
    
    
    for i, j in merge[r2 - 1][c2 - 1]:
        merge[i - 1][j - 1].append([r1, c1])
        if merge[r1 - 1][c1 - 1]:
            for val in merge[r1 - 1][c1 - 1]:
                merge[i - 1][j - 1].append(val)
    merge[r2 - 1][c2 - 1].append([r1, c1])

    for i, j in merge[r1 - 1][c1 - 1]:
        board[i - 1][j - 1] = board[r1 - 1][c1 - 1]
    
def UNMERGE(board, merge, order):
    _, r, c = order
    r, c = int(r), int(c)
    
    for i, j in merge[r - 1][c - 1]:
        merge[i - 1][j - 1] = []
        board[i - 1][j - 1] = "EMPTY"
    
def PRINT(board, order):
    _, r, c = order
    r, c = int(r), int(c)
    return board[r - 1][c - 1]

def solution(commands):
    answer = []
    board = [["EMPTY"] * 50 for _ in range(50)]
    merge = [[[] for i in range(50)] for j in range(50)]
    
    
    for command in commands:
        order = command.split()
        if order[0] == "UPDATE":
            if len(order) == 4:
                UPDATE(board, merge, order)
            else:
                UPDATEALL(board, order)
        elif order[0] == "MERGE":
            MERGE(board, merge, order)
        elif order[0] == "UNMERGE":
            UNMERGE(board, merge, order)
        else:
            answer.append(PRINT(board, order))
    
    print(answer)
    return answer