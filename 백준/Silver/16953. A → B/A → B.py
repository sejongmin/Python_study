import sys
from collections import deque
input = sys.stdin.readline

def solution(A: int, B: int) -> None:
    q = deque([(A, 1)])
    answer = -1
    while q:
        num, cnt = q.popleft()
        if num > B:
            continue
        if num == B:
            answer = cnt
            break
        
        q.append((num*2, cnt+1))
        q.append((num*10+1, cnt+1))

    print(answer)
    return

A, B = map(int, input().split())
solution(A, B)