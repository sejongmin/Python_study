def hour2minute(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def minute2hour(minute):
    h = minute // 60
    m = minute % 60
    return "%02d:%02d" %(h, m)

def solution(n, t, m, timetable):
    begin = hour2minute("09:00")
    buses = [i for i in range(begin, begin + t * n, t)]
    minutes = [hour2minute(time) for time in timetable]
    minutes.sort()
    
    for i in range(len(buses) - 1):
        arr = []
        while len(arr) < m:
            if not minutes:
                break
            if minutes[0] <= buses[i]:
                arr.append(minutes.pop(0))
            else:
                break
                
    if not minutes or minutes[0] > buses[-1] or len(minutes) < m or minutes[m - 1] > buses[-1]:
        return minute2hour(buses[-1])
    return minute2hour(minutes[m - 1] - 1)