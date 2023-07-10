import sys
read = sys.stdin.readline
schedule = []
answer = 0

N = int(read())
for _ in range(N):
    T, P = map(int, read().split())
    schedule.append((T, P))

def maxProfit(day, profit):
    for i in range(day, N):
        Ti, Pi = schedule[i]
        i += Ti
        if i <= N:
            profit += Pi
            maxProfit(i, profit)
            profit -= Pi
        i -= Ti
    global answer
    if answer < profit:
        answer = profit

maxProfit(0, 0)
print(answer)