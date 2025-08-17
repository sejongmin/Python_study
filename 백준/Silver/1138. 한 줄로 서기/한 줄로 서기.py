import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int, orders: list) -> None:
    q = deque([N])
    for i in range(N - 2, -1, -1):
        order = orders[i]
        q.insert(order, i + 1)
    print(*q)

if __name__ == "__main__":
    N = int(input())
    orders = list(map(int, input().split()))
    solution(N, orders)
