import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for a, b in zip(arr1[i], arr2[i]):
        print(a + b, end=" ")
    print()