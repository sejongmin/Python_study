N, S, R = map(int, input().split())

broken_num = list(map(int, input().split()))
afford_num = list(map(int, input().split()))

arr = [1 for _ in range(N)]
for i in broken_num:
    arr[i-1] -= 1
for i in afford_num:
    arr[i-1] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        if i != 0 and arr[i - 1] == 2:
            arr[i] += 1
            arr[i - 1] -= 1
        elif i != len(arr) - 1 and arr[i + 1] == 2:
            arr[i] += 1
            arr[i + 1] -= 1

print(arr.count(0))