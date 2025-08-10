import sys
input = sys.stdin.readline

def solution(p: int, m: int, players: list) -> None:
    rooms = [[players[0][0], 1, players[0]]]
    for i in range(1, p):
        level, nickname = players[i]
        flag = True
        for room in rooms:
            if room[1] < m and room[0] - 10 <= level <= room[0] + 10:
                room.append((level, nickname))
                room[1] += 1
                flag = False
                break
        if flag:
            rooms.append([level, 1, (level, nickname)])

    for room in rooms:
        if room[1] == m:
            print("Started!")
        else:
            print("Waiting!")
        for player in sorted(room[2:], key=lambda x: x[1]):
            print(*player)

if __name__ == "__main__":
    p, m = map(int, input().split())
    players = []
    for _ in range(p):
        l, n = input().split()
        players.append((int(l), n))
    solution(p, m, players)
