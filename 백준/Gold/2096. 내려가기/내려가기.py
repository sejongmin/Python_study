import sys
input = sys.stdin.readline

def solution(N):
    board = list(map(int, input().split()))
    dp_max = board[:]
    dp_min = board[:]
    for _ in range(1, N):
        board = list(map(int, input().split()))
        dp_max = [board[0] + max(dp_max[:2]), board[1] + max(dp_max), board[2] + max(dp_max[1:])]
        dp_min = [board[0] + min(dp_min[:2]), board[1] + min(dp_min), board[2] + min(dp_min[1:])]
    return max(dp_max), min(dp_min)

N = int(input())
print(*solution(N))