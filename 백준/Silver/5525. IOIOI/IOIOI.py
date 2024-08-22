import sys
input = sys.stdin.readline

def solution(N, L, S):
    answer = 0
    arr = list(S)
    label = ['I', 'O']
    for i in range(L - 2 * N):
        o = False
        if arr[i] == arr[i + 2 * N] == label[o]:
            flag = True
            for j in range(1, N + 1):
                o = not o
                if arr[i + j] == arr[i + 2 * N - j] == label[o]:
                    continue
                else:
                    flag=False
                    break
            if flag:
                answer += 1
    return answer

N = int(input())
L = int(input())
S = input().strip()
print(solution(N, L, S))