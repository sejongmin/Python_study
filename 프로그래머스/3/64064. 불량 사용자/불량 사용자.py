def dfs(arr, s, cnt, t):
    if cnt == len(arr):
        s.add(tuple(sorted(t)))
        return
        
    for i in range(len(arr[cnt])):
        if arr[cnt][i] in t:
            continue
        t.append(arr[cnt][i])
        dfs(arr, s, cnt + 1, t)
        t.remove(arr[cnt][i])

def solution(user_id, banned_id):
    arr = []
    for b in banned_id:
        possible = []
        for index in range(len(user_id)):
            if len(b) != len(user_id[index]):
                continue
            for i in range(len(b)):
                if b[i] != "*" and b[i] != user_id[index][i]:
                    break
            else:
                possible.append(index)
        arr.append(possible)
        
    s = set()
    t = list()
    dfs(arr, s, 0, t)
    
    return len(s)