import sys
input = sys.stdin.readline

def solution(N, parents, dnode):
    def remove(node):
        if not tree[node]:
            tree.pop(node, None)
            return
        for n in tree[node]:
            remove(n)
            tree.pop(node, None)

    answer = 0
    tree = {i: [] for i in range(N)}

    for i in range(N):
        if i == dnode:
            parent = parents[i]
        if parents[i] == -1:
            if i == dnode:
                print(0)
                return
        else:
            tree[parents[i]].append(i)
    tree[parent].remove(dnode)
    remove(dnode)

    for v in tree.values():
        if not len(v):
            answer += 1
    print(answer)

N = int(input())
parents = list(map(int, input().split()))
dnode = int(input())
solution(N, parents, dnode)