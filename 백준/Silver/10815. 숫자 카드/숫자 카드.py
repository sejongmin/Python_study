import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

answer = [0] * M
cards.sort()

for i in range(M):
    now = arr[i]
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] < now:
            left = mid + 1
        else:
            right = mid - 1
    if left < N and cards[left] == now:
        answer[i] = 1
    
print(*answer)

