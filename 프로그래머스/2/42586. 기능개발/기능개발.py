def solution(progresses, speeds):
    answer = []
    
    progresses
    
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count:
            answer.append(count)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return answer