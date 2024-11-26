import sys
input = sys.stdin.readline

def solution(n: int, numbers: list) -> None:
    class Node:
        def __init__(self, key, data=None) -> None:
            self.key = key
            self.data = data
            self.children = dict()
    
    class Trie:
        def __init__(self) -> None:
            self.root = Node(None)
        
        def insert(self, number):
            current = self.root

            for i in number:
                if not current.children.get(i, None):
                    current.children[i] = Node(i)
                current = current.children[i]
            
            current.data = number
        
        def consistency(self, number) -> bool:
            current = self.root

            for i in number:
                if current.data:
                    return False
                current = current.children[i]
            
            return True
    
    trie = Trie()
    for number in numbers:
        trie.insert(number)
    
    for number in numbers:
        if not trie.consistency(number):
            print('NO')
            return
    
    print('YES')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = []
    for i in range(n):
        number = list(map(int, input().strip()))
        numbers.append(number)
    solution(n, numbers)