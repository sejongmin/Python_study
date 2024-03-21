def solution(rows, columns, queries):
    answer = []
    board = [[j for j in range(j * columns + 1, (j + 1) * columns + 1)] for j in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        tmp1 = board[x1 - 1].pop(y2 - 1)
        board[x1 - 1].insert(y1 - 1, board[x1][y1 - 1])

        tmp2 = board[x2 - 1].pop(y1 - 1)
        board[x2 - 1].insert(y2 - 1, board[x2 - 2][y2 - 1])
        
        arr = board[x1 - 1][y1 - 1:y2] + board[x2 - 1][y1 - 1:y2]
        arr.append(tmp1)
        arr.append(tmp2)

        for i in range(x2 - 2, x1, -1):
            board[i][y2 - 1] = board[i - 1][y2 - 1]
            arr.append(board[i][y2 - 1])
        board[x1][y2 - 1] = tmp1

        for i in range(x1, x2 - 2):
            board[i][y1 - 1] = board[i + 1][y1 - 1]
            arr.append(board[i][y1 - 1])
        board[x2 - 2][y1 - 1] = tmp2
        
        answer.append(min(arr))

    return answer
        