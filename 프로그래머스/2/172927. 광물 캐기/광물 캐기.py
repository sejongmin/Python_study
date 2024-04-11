def fatigue(pick, minerals, idx):
    fatigue = 0
    left = 5 if len(minerals) >= idx + 5 else (len(minerals) - idx) % 5 
    if pick == 0:
        fatigue += left
    elif pick == 1:
        for i in range(left):
            if minerals[idx + i] == "diamond":
                fatigue += 5
            else:
                fatigue += 1
    elif pick == 2:
        for i in range(left):
            if minerals[idx + i] == "diamond":
                fatigue += 25
            elif minerals[idx + i] == "iron":
                fatigue += 5
            else:
                fatigue += 1
    return fatigue

def dfs(answer, picks, minerals, idx, score):
    if idx > len(minerals) or max(picks) == 0:
        answer = min(answer, score)
        return answer
    
    for i in range(3):
        if picks[i]:
            now = fatigue(i, minerals, idx)
            picks[i] -= 1
            answer = dfs(answer, picks, minerals, idx + 5, score + now)
            picks[i] += 1
    
    return answer

def solution(picks, minerals):
    answer = 10e5
    answer = dfs(answer, picks, minerals, 0, 0)
    return answer
    