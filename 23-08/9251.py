import sys
read = sys.stdin.readline

wordA = read().strip()
wordB = read().strip()
lenA = len(wordA)
lenB = len(wordB)
arr = [0] * lenB

for i in range(lenA):
    cnt = 0
    for j in range(lenB):
        if arr[j] > cnt:
            cnt = arr[j]
        elif wordA[i] == wordB[j]:
            arr[j] = cnt + 1

print(max(arr))