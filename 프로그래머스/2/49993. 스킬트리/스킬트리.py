def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        arr = list(st)
        index = 0
        while arr:
            s = arr.pop(0)
            if s in skill:
                if skill[index] == s:
                    index += 1
                    continue
                else:
                    arr.append(s)
                    break
        if not arr:
            answer += 1
    
    return answer