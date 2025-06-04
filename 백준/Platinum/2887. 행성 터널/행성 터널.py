import sys
import heapq
input = sys.stdin.readline

def solution(N, planets):
    def find(a):
        if a != parents[a]:
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parents[a] = b
        elif a < b:
            parents[b] = a

    answer = 0
    cnt = 0
    parents = [i for i in range(N)]
    x_planets = sorted(planets, key=lambda x: x[0])
    y_planets = sorted(planets, key=lambda x: x[1])
    z_planets = sorted(planets, key=lambda x: x[2])
    hq = []

    for i in range(N - 1):
        heapq.heappush(hq, (abs(x_planets[i][0] - x_planets[i + 1][0]), x_planets[i][3], x_planets[i + 1][3]))
        heapq.heappush(hq, (abs(y_planets[i][1] - y_planets[i + 1][1]), y_planets[i][3], y_planets[i + 1][3]))
        heapq.heappush(hq, (abs(z_planets[i][2] - z_planets[i + 1][2]), z_planets[i][3], z_planets[i + 1][3]))

    while cnt < N - 1:
        now, p1, p2 = heapq.heappop(hq)
        if find(p1) == find(p2):
            continue
        union(p1, p2)
        cnt += 1
        answer += now
    
    return answer

N = int(input())
planets = [list(map(int, input().split())) + [i] for i in range(N)]
print(solution(N, planets))
