def bfs(board, f):
    arr = []
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = [[False] * len(board[0]) for _ in range(len(board))]
    h, w = len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and board[i][j] == f:
                idx = 0
                q = [(i, j)]
                visit[i][j] = True
                while True:
                    if idx == len(q):
                        break
                    y, x = q[idx]
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if ny < 0 or nx < 0 or ny >= h or nx >= w:
                            continue
                        if not visit[ny][nx] and board[ny][nx] == f:
                            visit[ny][nx] = True
                            q.append((ny, nx))
                    idx += 1
                arr.append(q)
    return arr

def makeBlock(a):
    y, x = zip(*a)
    h, w = max(y) - min(y) + 1, max(x) - min(x) + 1
    block = [[0] * w for _ in range(h)]
    for i, j in a:
        block[i - min(y)][j - min(x)] = 1
    return block

def rotate(block):
    h, w = len(block), len(block[0])
    rBlock = [[0] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            rBlock[j][h - i - 1] = block[i][j]
    return rBlock
    
def isFit(block1, block2):
    h, w = len(block1), len(block1[0])
    if h != len(block2) or w != len(block2[0]):
        return False
    for i in range(h):
        if block1[i] != block2[i]:
            return False
    return True

def blockSize(block):
    cnt = 0
    for line in block:
        cnt += sum(line)
    return cnt

def solution(game_board, table):
    answer = 0
    board_empty = bfs(game_board, 0)
    table_piece = bfs(table, 1)
    board_block = []
    for i in board_empty:
        board_block.append(makeBlock(i))
    
    for i in table_piece:
        block = makeBlock(i)
        Flag = False
        for j in board_block:
            if Flag:
                break
            for k in range(4):
                block = rotate(block)
                if isFit(block, j):
                    board_block.remove(j)
                    answer += blockSize(j)
                    Flag = True
                    break
    return answer