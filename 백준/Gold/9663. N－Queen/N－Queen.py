import sys
input = sys.stdin.readline

N = int(input())
answer = 0

column_check = [False] * N
east_check = [False] * (2 * N - 1)
west_check = [False] * (2 * N - 1)

def dfs(r):
    global answer
    if r == N:
        answer += 1
        return
    
    for c in range(N):
        if column_check[c] or east_check[r + c] or west_check[r - c]:
            continue
        
        column_check[c] = True
        east_check[r + c] = True
        west_check[r - c] = True

        dfs(r + 1)

        column_check[c] = False
        east_check[r + c] = False
        west_check[r - c] = False

dfs(0)

print(answer)