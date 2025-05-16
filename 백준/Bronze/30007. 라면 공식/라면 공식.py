N = int(input())
for i in range(N):
    A, B, X = map(int, input().split())
    print((X - 1) * A + B)