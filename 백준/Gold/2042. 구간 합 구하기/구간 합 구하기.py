import sys
input = sys.stdin.readline

def solution(N, M, K, arr, queries):
    segment_tree = [0] * (N * 4)

    def init(start, end, index):
        if start == end:
            segment_tree[index] = arr[start - 1]
            return segment_tree[index]

        mid = (start + end) // 2
        segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
        return segment_tree[index]
    
    def update(start, end, index, update_index, update_value):
        if start > update_index or end < update_index:
            return
        
        segment_tree[index] += update_value

        if start == end:
            return
        
        mid = (start + end) // 2
        update(start, mid, index * 2, update_index, update_value)
        update(mid + 1, end, index * 2 + 1, update_index, update_value)
    
    def find(start, end, index, left, right):
        if start > right or end < left:
            return 0
        
        if start >= left and end <= right:
            return segment_tree[index]
        
        mid = (start + end) // 2
        sub_sum = find(start, mid, index * 2, left, right) + find(mid + 1, end, index * 2 + 1, left, right)
        return sub_sum
    
    init(1, N, 1)
    for a, b, c in queries:
        if a == 1:
            update(1, N, 1, b, c - arr[b - 1])
            arr[b - 1] = c
        elif a == 2:
            print(find(1, N, 1, b, c))

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
queries = [list(map(int, input().split())) for _ in range(M + K)]
solution(N, M, K, arr, queries)
