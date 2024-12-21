import sys
input = sys.stdin.readline

def solution(M: int, cocktail: list) -> None:
    ingredient = {}
    for s, x in cocktail:
        ingredient[s] = ingredient.get(s, 0) + int(x)
    
    values = list(ingredient.values())
    
    flag = False
    for i in range(len(values)):
        if flag:
            break
        for j in range(i + 1, len(values)):
            v1, v2 = values[i], values[j]
            if int(v1 * 1.618) == v2 or int(v2 * 1.618) == v1:
                flag = True
                break

    print("Delicious!" if flag else "Not Delicious...")

M = int(input())
cocktail = [input().split() for _ in range(M)]
solution(M, cocktail)
