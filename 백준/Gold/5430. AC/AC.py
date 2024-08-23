import sys
from collections import deque
input = sys.stdin.readline

def solution(p, n, x):
    if n:
        x = deque(x[1:-1].split(','))
    elif not n:
        x = deque([])
    order = True

    for f in p:
        if f == 'R':
            order = not order
        elif f == 'D':
            if x:
                if order:
                    x.popleft()
                elif not order:
                    x.pop()
            elif not x:
                print('error')
                return
    if not order:
        x = list(x)[::-1]
    print("["+','.join(x)+"]")

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    x = input().strip()
    solution(p, n, x)