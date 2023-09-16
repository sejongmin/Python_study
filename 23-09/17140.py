import sys
read = sys.stdin.readline

R, C, K = map(int, read().split())
arr = [list(map(int, read().split())) for i in range(3)]
answer = 0

def check(arr):
    if len(arr) >= R:
        if len(arr[R - 1]) >= C:
            if arr[R - 1][C - 1] == K:
                return True
    return False

def opR(arr):
    new_arr = [[] for i in range(len(arr))]
    max_length = 0
    for i in range(len(arr)):
        arr[i].sort()
        target = 1
        sumCnt = 0
        lenCnt = sum(arr[i])
        while sumCnt < lenCnt:
            targetNum = arr[i].count(target)
            if targetNum > 0:
                new_arr[i].append([target, targetNum])
                sumCnt += targetNum * target
            target += 1
        
        new_arr[i].sort(key=lambda x:x[1])
        if len(new_arr[i]) > 50:
            new_arr[i] = new_arr[i][0:50]
        arr[i] = []
        for j in range(len(new_arr[i])):
            arr[i].append(new_arr[i][j][0])
            arr[i].append(new_arr[i][j][1])
        max_length = max(max_length, len(arr[i]))
    for i in range(len(arr)):
        for j in range(max_length - len(arr[i])):
            arr[i].append(0)

def opC(arr):
    firstLen = len(arr)
    new_arr = [[] for i in range(len(arr[0]))]
    for i in range(len(arr[0])):
        target = 1
        sumCnt = 0
        lenCnt = 0
        for j in range(firstLen):
            lenCnt += arr[j][i]
        while sumCnt < lenCnt:
            targetNum = 0
            for j in range(firstLen):
                if arr[j][i] == target:
                    targetNum += 1
                    arr[j][i] = 0
            if targetNum > 0:
                new_arr[i].append([target, targetNum])
                sumCnt += targetNum * target
            target += 1
        
        new_arr[i].sort(key=lambda x:x[1])
        now = 0
        if len(new_arr[i]) > 50:
            new_arr[i] = new_arr[i][0:50]
        for j in range(len(new_arr[i])):
            for k in range(2):
                if now >= len(arr):
                    arr.append([0] * len(arr[0]))
                arr[now][i] = new_arr[i][j][k]
                now += 1

for i in range(101):
    if check(arr):
        break
    if len(arr) >= len(arr[0]):
        opR(arr)
    else:
        opC(arr)
    answer += 1
print(answer if answer < 101 else -1)