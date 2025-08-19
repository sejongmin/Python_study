import sys
input = sys.stdin.readline

def solution(N: int, balls: list) -> None:
    flag_b, flag_r = False, False
    cnt_r, cnt_b = 0, 0
    for i in range(N):
        if flag_b and balls[i] == 'R':
            cnt_r += 1
        if flag_r and balls[i] == 'B':
            cnt_b += 1
        if balls[i] == 'B':
            flag_b = True
        if balls[i] == 'R':
            flag_r = True
    answer = min(cnt_r, cnt_b)
    flag_b, flag_r = False, False
    cnt_r, cnt_b = 0, 0
    for i in range(N - 1, -1, -1):
        if flag_b and balls[i] == 'R':
            cnt_r += 1
        if flag_r and balls[i] == 'B':
            cnt_b += 1
        if balls[i] == 'B':
            flag_b = True
        if balls[i] == 'R':
            flag_r = True
    answer = min(answer, min(cnt_r, cnt_b))
    return answer

if __name__ == "__main__":
    N = int(input())
    balls = list(input().strip())
    print(solution(N, balls))
