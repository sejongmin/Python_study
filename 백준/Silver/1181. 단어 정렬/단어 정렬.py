import sys
input = sys.stdin.readline

def solution(N, words):
    words = list(set(words))
    words.sort(key=lambda x:(len(x), x))
    for word in words:
        print(word)

N = int(input())
words = [input().strip() for _ in range(N)]
solution(N, words)