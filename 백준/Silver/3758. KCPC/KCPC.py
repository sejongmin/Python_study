import sys
input = sys.stdin.readline

def solution(n: int, k: int, t: int, m: int, infos: list) -> int:
    teams = {i: [0] * (k + 2) for i in range(1, n + 1)}
    for i, (team, problem, score) in enumerate(infos):
        teams[team][0] += 1
        teams[team][-1] = i
        if teams[team][problem] < score:
            teams[team][problem] = score

    arr = [0] * (n)
    for team, v in teams.items():
        arr[team - 1] = (team, sum(v[1:-1]), v[0], v[-1])
    arr.sort(key=lambda x: (-x[1], x[2], x[3]))
    
    for i in range(n):
        if arr[i][0] == t:
            return i + 1

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, k, t, m = map(int, input().split())
        infos = [list(map(int, input().split())) for _ in range(m)]
        print(solution(n, k, t, m, infos))
