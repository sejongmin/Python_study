def solution(k, dungeons):
    answer = -1
    
    def back(visited, count):
        nonlocal answer, k, dungeons
        
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and i not in visited:
                k -= dungeons[i][1]
                visited.add(i)
                back(visited, count + 1)
                visited.remove(i)
                k += dungeons[i][1]
        
        answer = max(answer, count)
        
    back(set(), 0)
    return answer
