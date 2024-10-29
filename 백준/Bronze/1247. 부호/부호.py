import sys
input = sys.stdin.readline

for i in range(3):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    s = 0
    s = sum(arr)
    if s > 0:
        print("+")
    elif s < 0:
        print("-")
    elif s == 0:
        print("0")