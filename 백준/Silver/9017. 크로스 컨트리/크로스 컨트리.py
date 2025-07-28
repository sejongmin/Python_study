import sys
input = sys.stdin.readline

def solution(N: int, t: list) -> None:
    count = {}
    for v in t:
        count[v] = count.get(v, 0) + 1
    
    rank = 1
    team = {}
    for v in t:
        if count[v] == 6:
            if v not in team:
                team[v] = []
            team[v].append(rank)
            rank += 1

    min_val = int(1e9)
    winner = 0
    for k, v in team.items():
        if sum(v[:4]) < min_val:
            min_val = sum(v[:4])
            winner = k
        elif sum(v[:4]) == min_val:
            if team[winner][4] > team[k][4]:
                winner = k

    return winner

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        t = list(map(int, input().split()))
        print(solution(N, t))
