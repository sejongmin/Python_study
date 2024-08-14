import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

user_id_dict = {}
for i in range(N):
    url, user_id = input().strip().split()
    user_id_dict[url] = user_id

for i in range(M):
    url = input().strip()
    print(user_id_dict[url])