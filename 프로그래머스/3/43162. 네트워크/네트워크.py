def solution(n, computers):
    answer = 0
    
    q = []
    visit = [False] * n
    for i in range(n):
        if visit[i]:
            continue
        answer += 1
        q.append(i)
        visit[i] = True
        while q:
            now = q.pop(0)
            for idx in range(n):
                if visit[idx]:
                    continue
                if computers[now][idx]:
                    q.append(idx)
                    visit[idx] = True
            
    return answer