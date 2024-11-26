import sys
input = sys.stdin.readline

def solution(N, M, files, extensions):
    files.sort(key=lambda x:(x.split('.')[0], extensions.get(x.split('.')[1], 2), x.split('.')[1]))
    print(*files, sep="\n")

N, M = map(int, input().split())
files = [input().strip() for _ in range(N)]
extensions = {input().strip(): 1 for _ in range(M)}
solution(N, M, files, extensions)
