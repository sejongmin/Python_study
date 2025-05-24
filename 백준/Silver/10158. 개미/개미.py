import sys
input = sys.stdin.readline

def solution(w, h, p, q, t):
    # x 좌표 감소중
    if ((p + t - 1) // w) % 2 == 1:
        x = w - (p + t) % w if (p + t) % w else 0
    # x 좌표 증가중
    else:
        x = (p + t) % w if (p + t) % w else w
    # y 좌표 감소중
    if ((q + t - 1) // h) % 2 == 1:
        y = h - (q + t) % h if (q + t) % h else 0
    # y 좌표 증가중
    else:
        y = (q + t) % h if (q + t) % h else h

    print(x, y)

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
solution(w, h, p, q, t)