import sys
read = sys.stdin.readline

N = int(read().strip())
graph = [list(map(int, read().split())) for _ in range(N)]
start = 0
startTeam = []
answer = int(10e9)
visit = [False] * N

def DFS(n, now, start):
    if n == N // 2:
        linkTeam = []
        link = 0
        for i in range(N):
            if not visit[i]:
                linkTeam.append(i)
        for i in range(N // 2):
            for j in range(N // 2):
                link += graph[linkTeam[i]][linkTeam[j]]
        global answer
        answer = min(answer, abs(start - link))
        return

    i = now + 1
    while i < N:
        for j in range(len(startTeam)):
            start += graph[startTeam[j]][i]
            start += graph[i][startTeam[j]]
        startTeam.append(i)
        visit[i] = True
        DFS(n + 1, i, start)
        visit[i] = False
        startTeam.remove(i)
        for j in range(len(startTeam)):
            start -= graph[startTeam[j]][i]
            start -= graph[i][startTeam[j]]
        i += 1

DFS(0, -1, start)
print(answer)