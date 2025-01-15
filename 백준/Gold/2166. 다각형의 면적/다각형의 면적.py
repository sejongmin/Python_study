import sys
input = sys.stdin.readline

def solution(N: int, dots: list) -> float:
    answer = 0
    dots.append(dots[0])
    for i in range(N):
        answer += dots[i][0] * dots[i+1][1] - dots[i][1] * dots[i+1][0]
    
    answer = 0.5 * abs(answer)
    return answer

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, dots))
