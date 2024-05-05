import heapq

def solution(jobs):
    jobs.sort()
    
    time = 0
    i = 0
    process = []
    hq = []
    while i < len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(hq, (jobs[i][1], jobs[i][0]))
            i += 1
        if hq:
            t, start = heapq.heappop(hq)
            time += t
            process.append(time - start)
        else:
            time += 1
    while hq:
        t, start = heapq.heappop(hq)
        time += t
        process.append(time - start)
    
    return sum(process) // len(process)
        