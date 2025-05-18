import sys
input = sys.stdin.readline

def solution(N, board):
    black_group = []
    white_group = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if (i + j) % 2 == 0:
                    black_group.append((i, j))
                else:
                    white_group.append((i, j))

    def group_solve(group):
        def back(idx, rs, ls, res):
            nonlocal answer
            if len(group) == idx:
                if answer < res:
                    answer = res
                return
            right = group[idx][0] + group[idx][1]
            left = group[idx][0] - group[idx][1]

            back(idx + 1, rs, ls, res)
            if right not in rs and left not in ls:
                rs.add(right)
                ls.add(left)
                back(idx + 1, rs, ls, res + 1)
                rs.discard(right)
                ls.discard(left)

        answer = 0
        back(0, set(), set(), 0)
        return answer
    
    return group_solve(black_group) + group_solve(white_group)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
