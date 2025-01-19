import sys
input = sys.stdin.readline

def solution(N: int, players: list) -> list:
    answer = [0] * N
    cards = {player: idx for idx, player in enumerate(players)}
    max_num = max(players)

    for i in range(N):
        for num in range(players[i] * 2, max_num + 1, players[i]):
            if num in cards:
                answer[i] += 1
                answer[cards[num]] -= 1

    return answer

N = int(input())
players = list(map(int, input().split()))
print(*solution(N, players))