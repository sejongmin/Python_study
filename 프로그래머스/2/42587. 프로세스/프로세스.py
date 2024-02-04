def solution(priorities, location):
    answer = 0
    while True:
        process = priorities.pop(0)
        if priorities and max(priorities) > process:
            location = location - 1 if location > 0 else len(priorities)
            priorities.append(process)
        elif location > 0:
            location = location - 1 if location > 0 else len(priorities) - 1
            answer += 1
        elif location == 0:
            answer += 1
            break
        
    return answer