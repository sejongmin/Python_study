import sys
input = sys.stdin.readline

MOD = int(1e9) + 7
def solution(N, menu):
    answer = 0
    menu.sort()
    for i in range(N):
        answer += (menu[i] * (2 ** i - 2 ** (N - 1 - i))) % MOD
    
    return answer % MOD

N = int(input())
menu = list(map(int, input().split()))
print(solution(N, menu))
