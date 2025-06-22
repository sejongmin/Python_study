import sys
input = sys.stdin.readline

INF = int(1e6)
MOD = 1000000007

def solution(N: int, M: int, K: int, arr: list, queries: list) -> None:
    segment_tree = [1] * (N * 4)

    def create_segment_tree(start, end, index):
        if start == end:
            segment_tree[index] = arr[start]
            return segment_tree[index]
        
        mid = (start + end) // 2
        
        segment_tree[index] = (create_segment_tree(start, mid, index * 2) * create_segment_tree(mid + 1, end, index * 2 + 1)) % MOD
        return segment_tree[index]
    
    def update_segment_tree(start, end, index, value, value_index):
        if value_index < start or value_index > end:
            return segment_tree[index]

        if start == end:
            segment_tree[index] = value
            return segment_tree[index]

        mid = (start + end) // 2
        segment_tree[index] = (update_segment_tree(start, mid, index * 2, value, value_index) * update_segment_tree(mid + 1, end, index * 2 + 1, value, value_index)) % MOD
        return segment_tree[index]
    
    def find(start, end, index, left, right):
        if start > right or end < left:
            return 1
        
        if left <= start and right >= end:
            return segment_tree[index]

        else:
            mid = (start + end) // 2
            return (find(start, mid, index * 2, left, right) * find(mid + 1, end, index * 2 + 1, left, right)) % MOD

    create_segment_tree(0, N - 1, 1)
    for a, b, c in queries:
        if a == 1:
            update_segment_tree(0, N - 1, 1, c, b - 1)
        elif a == 2:
            print(find(0, N - 1, 1, b - 1, c - 1))
        

# N: 수의 개수 / M: 변경이 일어나는 횟수 / K: 구간의 곱 횟수
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(M + K)]
solution(N, M, K, arr, queries)
