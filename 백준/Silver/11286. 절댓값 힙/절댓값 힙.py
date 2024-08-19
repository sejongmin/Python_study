import sys
import heapq
input = sys.stdin.readline

def solution(N, x_list):
    h = []
    for i in range(N):
        if x_list[i] == 0:
            if h:
                v, s = heapq.heappop(h)
                print(v * (2 * s - 1))
            else:
                print(0)
        else:
            heapq.heappush(h, (abs(x_list[i]), (x_list[i] > 0)))

N = int(input())
x_list = [int(input()) for _ in range(N)]
solution(N, x_list)