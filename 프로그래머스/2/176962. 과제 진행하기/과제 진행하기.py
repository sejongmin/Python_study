def convertMinute(string):
    hour, minute = string.split(":")
    
    hour = int(hour)
    minute = int(minute)
    
    minute += hour * 60
    
    return minute

def solution(plans):
    answer = []
    arr = []
    stack = []
    
    for plan in plans:
        subjectName = plan[0]
        startTime = plan[1]
        duringTime = plan[2]
        
        startMin = convertMinute(startTime)
        
        arr.append([subjectName, startMin, int(duringTime)])
    
    arr.sort(key=lambda x:x[1])

    for i in range(len(arr)):
        now = arr[i][1] + arr[i][2]
        
        if i == len(arr) - 1:
            answer.append(arr[i][0])
        elif now > arr[i + 1][1]:
            stack.append([arr[i][0], arr[i][1] + arr[i][2] - arr[i + 1][1]])
        elif now <= arr[i + 1][1]:
            answer.append(arr[i][0])
            while stack:
                name, left = stack.pop()
                now += left
                if now <= arr[i + 1][1]:
                    answer.append(name)
                else:
                    stack.append([name, now - arr[i + 1][1]])
                    break

    while stack:
        name, left = stack.pop()
        answer.append(name)
        
    return answer