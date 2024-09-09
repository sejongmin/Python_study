import sys
input = sys.stdin.readline

def solution(N, K, M):
    answer = []
    people = [i for i in range(1, N + 1)]
    now = 0
    lef = N
    cnt = 0
    dir = K - 1

    while people:
        if cnt == M:
            dir = - dir - 1
            cnt = 0
        now = (now + dir) % lef
        answer.append(people.pop(now))
        lef -= 1
        cnt += 1
    
    print(*answer, sep="\n", end="")

N, K, M = map(int, input().split())
solution(N, K, M)
