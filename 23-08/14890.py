import sys
read = sys.stdin.readline

N, L = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
answer = 0

def findPath():
    global answer
    flag = True
    for i in range(N):
        flag = True
        before = 0
        after = 0
        for j in range(N - 1):
            if graph[i][j] == graph[i][j + 1]:
                if after:
                    after += 1
                else:
                    before += 1
            elif graph[i][j] + 1 == graph[i][j + 1]:
                if after:
                    if after >= 2 * L: 
                        before = 0
                        after = 0
                    else:
                        flag = False
                        break
                else:
                    if before >= L - 1:
                        before = 0
                    else:
                        flag = False
                        break                    
            elif graph[i][j] == graph[i][j + 1] + 1:
                before = 0
                if after:
                    if after >= L:
                        after = 0
                    else:
                        flag = False
                        break
                after += 1
            else:
                flag = False
                break
        if after:
            if after < L:
                flag = False
        if flag:
            answer += 1

    print(answer)
    
    flag = True
    for j in range(N):
        flag = True
        before = 0
        after = 0
        for i in range(N - 1):
            if graph[i][j] == graph[i + 1][j]:
                if after and after < L:
                    after += 1
                elif after == L:
                    after = 0
                else:
                    before += 1
            elif graph[i][j] + 1 == graph[i + 1][j]:
                if before + after >= L - 1: 
                    before = 0
                    after = 0
                else:
                    flag = False
                    break
            elif graph[i][j] == graph[i + 1][j] + 1:
                before = 0
                if after: 
                    if after >= L:
                        after = 0
                    else:
                        flag = False
                        break
                after += 1
            else:
                flag = False
                break
        if after:
            if after < L:
                flag = False
        if flag:
            answer += 1

findPath()
print(answer)