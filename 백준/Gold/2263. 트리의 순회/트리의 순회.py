import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def solution(n, in_order, post_order):
    in_order_idx = {in_order[i]: i for i in range(n)}
    def f(in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return
        root = post_order[post_right]
        print(root, end=' ')

        root_idx = in_order_idx[root]
        
        f(in_left, root_idx - 1, post_left, post_left + root_idx - in_left - 1)
        f(root_idx + 1, in_right, post_left + root_idx - in_left, post_right - 1)

    f(0, n-1, 0, n-1)

    return 1

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
solution(n, in_order, post_order)
