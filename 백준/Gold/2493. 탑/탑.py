import sys
input = sys.stdin.readline

def solution(N: int, tops: list) -> None:
    s = []
    answer = []
    for i, top in enumerate(tops):
        if not s:
            answer.append(0)
            s.append((i + 1, top))
            continue
        while s and s[-1][1] < top:
            s.pop()
        if s:
            answer.append(s[-1][0])
        else:
            answer.append(0)
        s.append((i + 1, top))

    print(*answer)

if __name__ == "__main__":
    N = int(input())
    tops = list(map(int, input().split()))
    solution(N, tops)