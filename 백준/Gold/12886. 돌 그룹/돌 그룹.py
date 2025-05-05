import sys
from collections import deque
input = sys.stdin.readline

def solution(A, B, C):
    total = A + B + C
    if total % 3:
        return 0
    
    q = deque([(min(A, B, C), max(A, B, C))])
    visited = [[False] * (total + 1) for _ in range(total + 1)]
    while q:
        x, y = q.popleft()
        z = total - x - y
        if x == y == z:
            return 1
        
        for a, b in [(x, y), (y, z), (z, x)]:
            if a > b:
                a -= b
                b += b
            elif a < b:
                b -= a
                a += a
            else:
                continue
            min_ = min(a, b, total - a - b)
            max_ = max(a, b, total - a - b)
            if not visited[min_][max_]:
                visited[min_][max_] = True
                q.append((min_, max_))
            
    return 0

A, B, C = map(int, input().split())
print(solution(A, B, C))
