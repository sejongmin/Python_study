import sys
input = sys.stdin.readline

def solution(N, L, S):
    answer = 0
    ioi = "IOI"

    i = 0
    count = 0
    while i < L - 2:
        if S[i:i+3] == ioi:
            count += 1
            i += 2
            if count == N:
                answer += 1
                count -= 1
        else:
            count = 0
            i += 1
    
    return answer

N = int(input())
L = int(input())
S = input().strip()
print(solution(N, L, S))