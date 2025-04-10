import sys
input = sys.stdin.readline

def solution(N, road, price):
    result = [False] * (N - 1)
    arr = [[i, v] for i, v in enumerate(price)]
    arr.pop()
    arr.sort(key=lambda x: x[1])

    for i, v in arr:
        j = i
        while j < N - 1 and not result[j]:
            result[j] = v * road[j]
            j += 1
    
    print(sum(result))

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
solution(N, road, price)