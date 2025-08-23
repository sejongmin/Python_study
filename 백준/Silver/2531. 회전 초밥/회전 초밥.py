import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int, d: int, k: int, c: int, dishes: list) -> int:
    answer = 0
    eat = deque([dishes[i] for i in range(N - k + 1, N)])

    for i in range(N):
        eat.append(dishes[i])
        res = 0
        kind = set(eat)
        if c not in kind:
            res += 1
        res += len(kind)
        answer = max(answer, res)
        eat.popleft()

    return answer

if __name__ == "__main__":
    N, d, k, c = map(int, input().split())
    dishes = [int(input()) for _ in range(N)]
    print(solution(N, d, k, c, dishes))
