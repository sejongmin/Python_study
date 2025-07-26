import sys
input = sys.stdin.readline

def solution(n: int, t: int, p: int, scores: list) -> int:
    scores.sort(reverse=True)

    rank = n + 1
    same_cnt = 0
    for i, score in enumerate(scores):
        if score < t:
            rank = i + 1
            break
        if score == t:
            same_cnt += 1
            continue
        same_cnt = 0
    
    if rank > p:
        return -1
    
    return rank - same_cnt

if __name__ == "__main__":
    n, t, p = map(int, input().split())
    scores = []
    if n:
        scores = list(map(int, input().split()))
    print(solution(n, t, p, scores))
