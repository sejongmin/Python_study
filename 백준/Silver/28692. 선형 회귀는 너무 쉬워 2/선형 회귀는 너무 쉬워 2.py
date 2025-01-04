import sys
input = sys.stdin.readline

def solution(n: int, dots: list) -> None:
    sx = 0
    sy = 0
    sxx = 0
    sxy = 0
    for x, y in dots:
        sx += x
        sy += y
        sxx += x * x
        sxy += x * y
    if n * sxx == sx * sx:
        print("EZPZ")
        return
    a = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    b = (sy - a * sx) / n
    print(a, b)
    
n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append((x, y))
solution(n, dots)
    