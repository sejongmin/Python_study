import sys
input = sys.stdin.readline

def solution(N, M, arr, parites):
    true_party = set()
    visited = [False] * (N + 1)
    people = {i:[] for i in range(1, N + 1)}
    for i, party in enumerate(parties):
        for j in range(1, party[0] + 1):
            people[party[j]].append(i)
    
    q = []
    for i in range(1, arr[0] + 1):
        q.append(arr[i])
        visited[arr[i]] = True
        for party in people[arr[i]]:
            true_party.add(party)
    
    while q:
        p = q.pop()
        for i in people[p]:
            for j in range(1, parties[i][0] + 1):
                if not visited[parties[i][j]]:
                    q.append(parties[i][j])
                    visited[parties[i][j]] = True
            true_party.add(i)

    return M - len(true_party)


N, M = map(int, input().split())
arr = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, arr, parties))