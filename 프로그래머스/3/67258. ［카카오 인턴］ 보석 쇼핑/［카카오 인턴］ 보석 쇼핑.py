def solution(gems):
    count = len(set(gems))
    gems_dict = {}
    candidate = []
    left = -1
    
    for right, gem in enumerate(gems):
        gems_dict[gem] = gems_dict.get(gem, 0) + 1
        while len(gems_dict) == count:
            left += 1
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                del gems_dict[gems[left]]
                candidate.append((left + 1, right + 1))
                break
    print(candidate)
    return sorted(candidate, key=lambda x:x[1] - x[0])[0]
                
                