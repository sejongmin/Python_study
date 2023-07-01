import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr)

min = 200000

for i in range(n):
    s = arr[i] + arr[len(arr) - i - 1]
    if (s < min):
        min = s

print(min)