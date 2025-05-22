import sys
input = sys.stdin.readline

def solution(a, b):
    d = {
        1: {0, 1, 5, 6},
        2: {4, 9},
        4: {2, 3, 7, 8},
    }

    now = a % 10
    if now in d[1]:
        print(now if now > 0 else 10)
    elif now in d[2]:
        if b % 2:
            print(now)
        else:
            print(now ** 2 % 10)
    elif now in d[4]:
        if b % 4 == 1:
            print(now)
        elif b % 4 == 2:
            print(now ** 2 % 10)
        elif b % 4 == 3:
            print(now ** 3 % 10)
        else:
            print(now ** 4 % 10)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    solution(a, b)
