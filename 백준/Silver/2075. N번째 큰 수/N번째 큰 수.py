import sys
import heapq
input = sys.stdin.readline

def solution(N: int) -> int:
    hq = []
    line = list(map(int, input().split()))
    for i in range(N):
        heapq.heappush(hq, line[i])
    
    for i in range(1, N):
        line = list(map(int, input().split()))
        for j in range(N):
            if hq[0] < line[j]:
                heapq.heappush(hq, line[j])
                heapq.heappop(hq)
    return hq[0]

if __name__ == "__main__":
    N = int(input())
    print(solution(N))
