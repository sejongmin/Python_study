import sys
input = sys.stdin.readline

def solution(N: int, stock: list) -> int:
    answer = 0
    top = 0
    for i in range(N - 1, -1, -1):
        price = stock[i]
        if price > top:
            top = price
        else:
            answer += top - price
    return answer

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        stock = list(map(int, input().split()))
        print(solution(N, stock))
