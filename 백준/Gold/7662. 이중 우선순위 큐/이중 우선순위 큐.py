import sys
import heapq
input = sys.stdin.readline

def solution(K):
    answer_min, answer_max = 0, 0
    min_heap = []
    max_heap = []
    check = [False] * K
    cnt = 0

    for i in range(K):
        op, n = input().strip().split()
        n = int(n)

        if op == 'I':
            cnt += 1
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
        elif op == 'D':
            cnt = max(0, cnt-1)
            if n == -1:
                while min_heap:
                    _, idx = heapq.heappop(min_heap)
                    if not check[idx]:
                        check[idx] = True
                        break
            elif n == 1:
                while max_heap:
                    _, idx = heapq.heappop(max_heap)
                    if not check[idx]:
                        check[idx] = True
                        break
    while min_heap:
        answer_min, idx = heapq.heappop(min_heap)
        if not check[idx]:
            break
    while max_heap:
        answer_max, idx = heapq.heappop(max_heap)
        if not check[idx]:
            break
    if cnt:
        print(-answer_max, answer_min)
    else:
        print("EMPTY")

T = int(input())
for _ in range(T):
    K = int(input())
    solution(K)