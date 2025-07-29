import sys
input = sys.stdin.readline

def solution(N: int, M: int, streetlight: list) -> int:
    answer = max(streetlight[0], N - streetlight[-1])
    for i in range(1, M):
        answer = max(answer, (streetlight[i] - streetlight[i - 1] + 1) // 2)
    return answer

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    streetlight = list(map(int, input().split()))
    print(solution(N, M, streetlight))
