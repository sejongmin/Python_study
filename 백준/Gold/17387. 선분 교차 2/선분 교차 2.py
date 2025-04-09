import sys
input = sys.stdin.readline

def solution(L1, L2):
    def ccw(x1, y1, x2, y2, x3, y3):
        return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3
        
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2
    a = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    b = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    if a > 0 or b > 0:
        return 0
    elif a == 0 and b == 0:
        if min(x1, x2) <= max(x3, x4) and min(y1, y2) <= max(y3, y4) and min(x3, x4) <= max(x1, x2) and min(y3, y4) <= max(y1, y2):
            return 1
        else:
            return 0
    else:
        return 1


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
print(solution(L1, L2))
