import sys
input = sys.stdin.readline

m, r, c = 0, 0, 0
arr = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    a = max(arr[i])
    if m < a:
        m = a
        r = i
        c = arr[i].index(m)

print(m)
print(r + 1, c + 1)