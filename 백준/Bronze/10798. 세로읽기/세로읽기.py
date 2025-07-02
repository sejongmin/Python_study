import sys
input = sys.stdin.readline

def solution(arr):
    for i in range(5):
        now = len(arr[i])
        while now < 15:
            now += 1
            arr[i].append('')
    
    answer = ''
    for i in range(15):
        for j in range(5):
            answer += arr[j][i]

    print(answer)

arr = [list(input().strip()) for _ in range(5)]
solution(arr)