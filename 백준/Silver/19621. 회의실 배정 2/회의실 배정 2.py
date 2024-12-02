import sys
input = sys.stdin.readline

def solution(N, meetings):
    answer = 0
    meetings.sort(key=lambda x:x[1])
    def back(idx, now):
        nonlocal answer
        for i in range(idx + 1, N):
            if meetings[idx][1] <= meetings[i][0]:
                back(i, now + meetings[i][2])
        answer = max(answer, now)
    
    for i in range(N):
        back(i, meetings[i][2])
    
    print(answer)

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
solution(N, meetings)
