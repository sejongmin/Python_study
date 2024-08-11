import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    order = input().split()
    if order[0] == "add":
        if order[1] not in S:
            S.add(order[1])
    elif order[0] == "remove":
        if order[1] in S:
            S.remove(order[1])
    elif order[0] == "check":
        if order[1] in S:
            print("1")
        else:
            print("0")
    elif order[0] == "toggle":
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == "all":
        S = {str(i) for i in range(1, 21)}
    elif order[0] == "empty":
        S = set()
    