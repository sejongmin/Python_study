import sys
input = sys.stdin.readline

def solution(N: int, tunnels: list) -> None:
    class Node:
        def __init__(self):
            self.children = dict()
            self.is_final = False

    class Trie:
        def __init__(self):
            self.root = Node()
        
        def insert(self, tunnel: list):
            curr_node = self.root

            for t in tunnel:
                if curr_node.children.get(t) is None:
                    curr_node.children[t] = Node()
                curr_node = curr_node.children[t]
            curr_node.is_final = True
    
        def travel(self):
            def dfs(prefix, curr_node):
                if curr_node.is_final:
                    return
                for t in sorted(curr_node.children):
                    print(prefix + t)
                    dfs(prefix + '--', curr_node.children[t])

            dfs('', self.root)

    trie = Trie()
    for tunnel in tunnels:
        trie.insert(tunnel[1:])
    trie.travel()

N = int(input())
tunnels = [list(input().strip().split()) for _ in range(N)]
solution(N, tunnels)
