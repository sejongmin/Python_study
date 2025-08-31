import sys
input = sys.stdin.readline

def solution(N: int, arr: list) -> None:
    result = []
    def dfs(v, i):
        visited[v] = True
        w = arr[v]
        if not visited[w]:
            dfs(w, i)
        elif visited[w] and w == i:
            result.append(w)

    for i in range(1, N + 1):
        visited = [False] * 101
        dfs(i, i)

    print(len(result))
    print(*sorted(result), sep='\n')

if __name__ == "__main__":
    N = int(input())
    arr = [0] + [int(input()) for _ in range(N)]
    solution(N, arr)
