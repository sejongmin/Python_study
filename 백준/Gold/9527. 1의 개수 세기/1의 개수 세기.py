import sys
import math
input = sys.stdin.readline

def solution(A: int, B: int) -> int:
    def get_one_cnt(n):
        if n < 1:
            return 0
        a = int(math.log2(n))
        if n == 2 ** a:
            return a * n // 2 + 1
        
        return get_one_cnt(2 ** a) + get_one_cnt(n - 2 ** a) + n - 2 ** a

    return get_one_cnt(B) - get_one_cnt(A - 1)

A, B = map(int, input().split())
print(solution(A, B))
