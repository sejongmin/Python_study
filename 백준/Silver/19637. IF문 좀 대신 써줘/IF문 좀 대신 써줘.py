import sys
input = sys.stdin.readline

def solution(N: int, M: int, titles: list, powers: list) -> None:
    for power in powers:
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            title = int(titles[mid][1])
            if power <= title:
                right = mid - 1
            elif power > title:
                left = mid + 1
        
        print(titles[left][0])

if __name__ == "__main__":
    N, M = map(int, input().split())
    titles = [input().split() for _ in range(N)]
    powers = [int(input()) for _ in range(M)]
    solution(N, M, titles, powers)
