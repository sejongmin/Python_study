import sys
input = sys.stdin.readline

def solution(N: int, candies: list) -> None:
    s = sum(candies)
    if s % N:
        print("NO")
    else:
        print("YES")

T = int(input())
for _ in range(T):
    tmp = input().strip()
    N = int(input())
    candies = []
    for i in range(N):
        candy = int(input())
        candies.append(candy)
    solution(N, candies)