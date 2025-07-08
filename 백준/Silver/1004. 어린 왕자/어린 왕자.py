import sys
import math
input = sys.stdin.readline

def solution(x1, y1, x2, y2, n, planets):
    def is_inside(cx, cy, r, x, y):
        if r < math.sqrt(pow((cx - x), 2) + pow((cy - y), 2)):
            return False
        return True
    
    answer = 0
    for cx, cy, r in planets:
        start_inside = is_inside(cx, cy, r, x1, y1)
        end_inside = is_inside(cx, cy, r, x2, y2)
        if start_inside != end_inside:
            answer += 1
    return answer

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]
    print(solution(x1, y1, x2, y2, n, planets))