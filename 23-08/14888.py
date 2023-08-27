import sys
read = sys.stdin.readline

N = int(read().strip())
arr = list(map(int, read().split()))
op = list(map(int, read().split()))
answer_max = -int(10e9)
answer_min = int(10e9)

def DFS(n, index, now):
    if n == N:
        global answer_max, answer_min
        answer_max = max(answer_max, now)
        answer_min = min(answer_min, now)
        return

    for i in range(4):
        if op[i] == 0:
            continue
        op[i] -= 1
        if i == 0:
            now += arr[index]
            DFS(n + 1, index + 1, now)
            now -= arr[index]
        if i == 1:
            now -= arr[index]
            DFS(n + 1, index + 1, now)
            now += arr[index]
        if i == 2:
            now *= arr[index]
            DFS(n + 1, index + 1, now)
            now //= arr[index]
        if i == 3:
            if now < 0:
                now = -now
                remain = now % arr[index]
                now //= arr[index]
                DFS(n + 1, index + 1, -now)
                now *= arr[index]
                now += remain
                now = -now
            else:
                remain = now % arr[index]
                now //= arr[index]
                DFS(n + 1, index + 1, now)
                now *= arr[index]
                now += remain
        op[i] += 1

DFS(1, 1, arr[0])
print(answer_max)
print(answer_min)