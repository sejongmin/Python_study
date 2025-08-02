import sys
input = sys.stdin.readline

def solution(N: int, X: int, visit: list) -> None:
    now = sum(visit[:X])
    max_visit = now
    count = 1

    for i in range(N - X):
        now = now - visit[i] + visit[i + X]
        if max_visit < now:
            max_visit = now
            count = 1
        elif max_visit == now:
            count += 1

    if max_visit:
        print(max_visit)
        print(count)
    else:
        print("SAD")

if __name__ == "__main__":
    N, X = map(int, input().split())
    visit = list(map(int, input().split()))
    solution(N, X, visit)
