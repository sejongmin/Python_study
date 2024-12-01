import sys
input = sys.stdin.readline

def solution(n, n_tuple):
    visited = set()
    visited.add(tuple(n_tuple))
    new_tuple = n_tuple
    for _ in range(1000):
        new_tuple = list(map(lambda x, y: abs(x - y), new_tuple, new_tuple[1:] + new_tuple[:1]))
        if sum(new_tuple) == 0:
            print("ZERO")
            return
    print("LOOP")
    return


T = int(input())
for _ in range(T):
    n = int(input())
    n_tuple = list(map(int, input().split()))
    solution(n, n_tuple)