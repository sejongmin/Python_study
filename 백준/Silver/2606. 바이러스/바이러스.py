import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
computer = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    computer[start].append(end)
    computer[end].append(start)

def solution(computer):
    answer = 0
    stack = computer[1][:]
    visited = set([1])
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            answer += 1
            stack.extend(computer[current])
    return answer

print(solution(computer))