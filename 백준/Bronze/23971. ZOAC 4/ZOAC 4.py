import sys
import math
input = sys.stdin.readline

def solution(H, W, N, M):
    return math.ceil((H / (N + 1))) * math.ceil(W / (M + 1))
    
H, W, N, M = map(int, input().split())
print(solution(H, W, N, M))
