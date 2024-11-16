import sys
from collections import deque
input = sys.stdin.readline

N = int(input())


stack = deque()
top = -1
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stack.append(order[1])
        top += 1
    elif order[0] == 2:
        if top >= 0:
            top -= 1
            print(stack.pop())
        else:
            print("-1")
    elif order[0] == 3:
        print(top + 1)
    elif order[0] == 4:
        if top >= 0:
            print(0)
        else:
            print(1)
    elif order[0] == 5:
        if top >= 0:
            print(stack[top])
        else:
            print("-1")