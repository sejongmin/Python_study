import sys
import heapq
input = sys.stdin.readline

def solution(n, ho, d):
    answer = 0
    roads = []
    for i in range(n):
        if d < abs(ho[i][1] - ho[i][0]):
            continue
        roads.append(sorted(ho[i]))
    roads.sort(key=lambda x: x[1])

    hq = []
    cnt = 0
    for s, e in roads:
        while hq and hq[0][0] < e - d:
            heapq.heappop(hq)
            cnt -= 1
        heapq.heappush(hq, (s, e))
        cnt += 1
        answer = max(answer, cnt)
        
    return answer

n = int(input())
ho = [list(map(int, input().split())) for _ in range(n)]
d = int(input())
print(solution(n, ho, d))
