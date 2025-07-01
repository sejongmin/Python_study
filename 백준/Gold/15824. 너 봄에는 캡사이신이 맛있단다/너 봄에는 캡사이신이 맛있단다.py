import sys
input = sys.stdin.readline

MOD = int(1e9) + 7
def solution(N, menu):
    answer = 0
    menu.sort()
    pow_cache = [1] * N
    for i in range(1, N):
        pow_cache[i] = pow_cache[i - 1] * 2

    for i in range(N):
        answer += (menu[i] * (pow_cache[i] - pow_cache[N - 1 - i])) % MOD
    
    return answer % MOD

N = int(input())
menu = list(map(int, input().split()))
print(solution(N, menu))
