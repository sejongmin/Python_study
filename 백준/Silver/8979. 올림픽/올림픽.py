import sys
input = sys.stdin.readline

def solution(N: int, K: int, countries: list) -> int:
    countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    medals = set()
    rank = 0
    same = 1
    for c, g, s, b in countries:
        if (g, s, b) in medals:
            same += 1
        else:
            rank += same
            same = 1
            medals.add((g, s, b))
        if c == K:
            return rank

if __name__ == "__main__":
    N, K = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, K, countries))
