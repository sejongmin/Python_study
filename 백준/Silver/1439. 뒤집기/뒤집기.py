import sys
input = sys.stdin.readline

def solution(S):
    cnt = [0, 0]
    now = S[0]
    for i in range(1, len(S)):
        if now != S[i]:
            cnt[int(now)] += 1
            now = S[i]
    cnt[int(now)] += 1
    return min(cnt)

S = list(input().strip())
print(solution(S))