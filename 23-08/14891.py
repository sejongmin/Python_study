import sys
read = sys.stdin.readline

gear = [list(map(int, input())) for _ in range(4)]
T = int(read().strip())

def rotate(n, d):
    if d == 0:
        return
    
    if d == 1:
        tmp = gear[n].pop(7)
        gear[n].insert(0, tmp)
    elif d == -1:
        tmp = gear[n].pop(0)
        gear[n].append(tmp)

def sol(T):
    answer = 0
    for _ in range(T):
        r = [0] * 4
        n, d = map(int, read().split())

        r[n - 1] = d
        while n < 4 and gear[n - 1][2] != gear[n][6]:
            r[n] = -r[n - 1]
            n += 1
        while n > 1 and gear[n - 1][6] != gear[n - 2][2]:
            n -= 1
            r[n - 1] = -r[n]
        
        for i in range(4):
            rotate(i, r[i])
    for i in range(4):
        answer += gear[i][0] * 2 ** i
    print(answer)

sol(T)