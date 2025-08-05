import sys
input = sys.stdin.readline

def solution(N: int, words: list) -> int:
    answer = 0
    alpha = [0] * 26
    for c in words[0]:
        alpha[ord(c) - ord('A')] += 1

    for i in range(1, N):
        word = words[i]
        cnt = 0
        word_hash = {}
        for c in word:
            word_hash[ord(c) - ord('A')] = word_hash.get(ord(c) - ord('A'), 0) + 1
        
        for i in range(26):
            cnt += abs(alpha[i] - word_hash.get(i, 0))
        if cnt < 2:
            answer += 1
        elif len(word) == len(words[0]) and cnt == 2:
            answer += 1
    return answer

if __name__ == "__main__":
    N = int(input())
    words = [input().strip() for _ in range(N)]
    print(solution(N, words))
