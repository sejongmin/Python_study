import sys
input = sys.stdin.readline

def solution(N):
    tree = {}
    for _ in range(N):
        parent, left, right = input().split()
        tree[parent] = [left, right]
    def preOrder(tree, now):
        if now == ".":
            return
        print(now, end="")
        preOrder(tree, tree[now][0])
        preOrder(tree, tree[now][1])

    def inOrder(tree, now):
        if now == ".":
            return
        inOrder(tree, tree[now][0])
        print(now, end="")
        inOrder(tree, tree[now][1])

    def postOrder(tree, now):
        if now == ".":
            return
        postOrder(tree, tree[now][0])
        postOrder(tree, tree[now][1])
        print(now, end="")

    preOrder(tree, "A")
    print()
    inOrder(tree, "A")
    print()
    postOrder(tree, "A")

N = int(input())
solution(N)