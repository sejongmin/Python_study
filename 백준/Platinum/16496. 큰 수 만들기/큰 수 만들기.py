import sys
input = sys.stdin.readline

def solution(N: int, arr: list) -> str:
    new_arr = [[arr[i], arr[i]] for i in range(N)]
    max_len = 10
    
    for i in range(N):
        l = len(new_arr[i][0])
        k = 0
        while l < max_len:
            new_arr[i][1] += new_arr[i][0][k % len(new_arr[i][0])]
            l += 1
            k += 1
    
    new_arr.sort(key=lambda x: x[1])
    new_arr.reverse()

    answer = ''
    for i in range(N):
        answer += new_arr[i][0]

    return int(answer)

N = int(input())
arr = input().split()
print(solution(N, arr))

