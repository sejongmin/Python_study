import sys
import heapq
input = sys.stdin.readline

def solution(N, x_list):
    h = []
    for x in x_list:
        if x == 0:
            if h:
                print(-heapq.heappop(h))
            else:
                print(0)
        elif x != 0:
            heapq.heappush(h, -x)

N = int(input())
x_list = [int(input()) for _ in range(N)]
solution(N, x_list)