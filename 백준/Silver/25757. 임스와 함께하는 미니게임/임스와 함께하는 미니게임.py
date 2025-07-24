game = {
    'Y': 1,
    'F': 2,
    'O': 3
}

N, M = input().strip().split()
answer = 0
users = set()
cnt = 0

for _ in range(int(N)):
    u = input().strip()
    if u not in users:
        users.add(u)
        cnt += 1
        if game[M] == cnt:
            cnt = 0
            answer += 1
print(answer)
            