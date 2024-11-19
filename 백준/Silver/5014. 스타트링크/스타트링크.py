import sys
from collections import deque

def solution(F, S, G, U, D):
    answer = -1
    visit = set()
    q = deque()

    visit.add(S)
    q.append((S, 0))

    while q:
        now, click = q.popleft()
        if now == G:
            answer = click
            break
        if now + U <= F and now + U not in visit:
            q.append((now + U, click + 1))
            visit.add(now + U)
        if now - D > 0 and now - D not in visit:
            q.append((now - D, click + 1))
            visit.add(now - D)

    return answer if answer >= 0 else "use the stairs"

F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))