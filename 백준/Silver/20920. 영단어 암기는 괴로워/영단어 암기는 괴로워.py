import sys
input = sys.stdin.readline

def solution(N: int, M: int, words: list):
    word_dict = {}
    for word in words:
        if len(word) < M:
            continue
        if word not in word_dict:
            word_dict[word] = [0, len(word), word]
        word_dict[word][0] += 1
    
    for _, _, v in sorted(word_dict.values(), key=lambda x: (-x[0], -x[1], x[2])):
        print(v)
    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    words = [input().rstrip() for _ in range(N)]
    solution(N, M, words)
