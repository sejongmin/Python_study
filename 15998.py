import sys
read = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

N = int(read())
flag = True
maxval = 0
before = 0
M = 0

for _ in range(N):
    money, balance = map(int, read().split())
    if flag == False:
        continue
    if before + money < 0:
        tM = balance - before - money
        if M == 0:
            M = tM
        P = gcd(tM, M)
        if maxval < balance:
            maxval = balance
        if maxval < P:
            M = P
        else:
            flag = False
        before = balance

    elif before + money >= 0:
        if before + money != balance:
            flag = False
        before = balance

if flag:
    if M == 0:
        print(1)
    else:
        print(M)
else:
    print(-1)