import sys
input = sys.stdin.readline

def solution(n, m, keywords, posts) -> None:
    answer = []
    for post in posts:
        for word in post:
            if word in keywords:
                keywords.discard(word)
        answer.append(len(keywords))
    print(*answer, sep='\n')

if __name__ == "__main__":
    n, m = map(int, input().split())
    keywords = set([input().strip() for _ in range(n)])
    posts = [input().strip().split(',') for _ in range(m)]
    solution(n, m, keywords, posts)
