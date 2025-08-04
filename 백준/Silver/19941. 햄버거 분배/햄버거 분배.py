import sys
input = sys.stdin.readline

def solution(N: int, K: int, desk: list) -> int:
    eat = [0] * N
    for i in range(N):
        if desk[i] == 'P':
            for j in range(max(0, i - K), min(i + K + 1, N)):
                if desk[j] == 'H' and eat[j] == 0:
                    eat[j] = 1
                    break
    return sum(eat)

if __name__ == "__main__":
    N, K = map(int, input().split())
    desk = list(input().strip())
    print(solution(N, K, desk))

