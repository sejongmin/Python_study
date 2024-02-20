import re
import copy

def cal(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b

def dfs(operators, answer, arr):
    if len(arr) == 1:
        return max(answer, abs(int(arr[0])))
    
    
    for op in operators:
        if op not in arr:
            continue
        new_arr = copy.deepcopy(arr)
        while op in new_arr:
            i = new_arr.index(op)
            a = new_arr.pop(i - 1)
            new_arr.pop(i - 1)
            b = new_arr.pop(i - 1)
            n = cal(int(a), int(b), op)
            new_arr.insert(i - 1, str(n))
        
        answer = dfs(operators, answer, new_arr)
    
    return answer
    
def solution(expression):
    answer = 0
    operators = ["+", "-", "*"]
    arr = re.split('([^0-9])', expression)

    for op in operators:
        if not op in arr:
            operators.remove(op)

    answer = dfs(operators, 0, arr)
    
    return answer