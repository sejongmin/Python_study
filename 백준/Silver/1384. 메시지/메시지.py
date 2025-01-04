import sys
input = sys.stdin.readline

def solution(group: int, n: int, arr: list) -> None:
    answer = []
    for i in range(n):
        for j in range(1, n):
            if arr[i][j] == 'N':
                answer.append((arr[i - j][0], arr[i][0]))
    print("Group", group)
    if answer:
        for a, b in answer:
            print(a, "was nasty about", b)
    else:
        print("Nobody was nasty")
    print()

group = 0
while n := int(input()):
    group += 1
    arr = []
    for i in range(n):
        info = input().strip().split()
        arr.append(info)
    solution(group, n, arr)