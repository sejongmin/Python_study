import sys
input = sys.stdin.readline

def solution(paper: str) -> None:
    now = list(paper)
    while len(now) >= 3:
        next = []
        for i in range(len(now) - 1):
            if i % 2 == 0:
                if now[i] == now[i + 2]:
                    print("NO")
                    return
            if i % 2 == 1:
                next.append(now[i])
        now = next[:]
    print("YES")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        paper = input().strip()
        solution(paper)