import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_name = {}
pokemon_number = {}
for i in range(1, N + 1):
    pokemon = input().strip()
    pokemon_number[i] = pokemon
    pokemon_name[pokemon] = i

for i in range(M):
    q = input().strip()
    if '0' <= q[0] <= '9':
        print(pokemon_number[int(q)])
    else:
        print(pokemon_name[q])