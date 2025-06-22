import sys
input = sys.stdin.readline

INF = int(1e9)

def solution(N, M, arr, pairs):
    segment_tree = [(INF, 0)] * (N * 4)

    def make_segment_tree(start, end, index):
        if start == end:
            segment_tree[index] = (arr[start], arr[start])
            return segment_tree[index]

        mid = (start + end) // 2
        left_child = make_segment_tree(start, mid, index * 2)
        right_child = make_segment_tree(mid + 1, end, index * 2 + 1)

        segment_tree[index] = (min(left_child[0], right_child[0]), max(left_child[1], right_child[1]))
        return segment_tree[index]
    
    def find(start, end, index, a, b):
        if a > end or b < start:
            return (INF, 0)
        
        mid = (start + end) // 2

        if a <= start and end <= b:
            return segment_tree[index]
        
        else:
            left = find(start, mid, index * 2, a, b)
            right = find(mid + 1, end, index * 2 + 1, a, b)
            return (min(left[0], right[0]), max(left[1], right[1]))
    
    make_segment_tree(0, N - 1, 1)
    for a, b in pairs:
        res = find(0, N - 1, 1, a - 1, b - 1)
        print(res[0], res[1])

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
pairs = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, arr, pairs)
