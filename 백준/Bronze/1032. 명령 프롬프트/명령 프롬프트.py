import sys
input = sys.stdin.readline

def solution(N, s):
    length = len(s[0])
    answer = ['?'] * length

    for i in range(length):
        now = s[0][i]
        for j in range(1, N):
            if now != s[j][i]:
                now = False
                break
        if now:
            answer[i] = now
    print(''.join(answer))

N = int(input())
s = [input().strip() for _ in range(N)]
solution(N, s)
