import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = []
    C = int(input())
    answer.append(C // 25)
    C = C % 25
    answer.append(C // 10)
    C = C % 10
    answer.append(C // 5)
    C = C % 5
    answer.append(C)
    print(*answer)