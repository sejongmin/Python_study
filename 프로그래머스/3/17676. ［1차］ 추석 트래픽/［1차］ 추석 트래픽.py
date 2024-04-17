def convertSecond(time, duration):
    h, m, s = time.split(":")
    end = float(s) * 1000
    end += (int(m) * 60) * 1000
    end += (int(h) * 3600) * 1000
    
    duration = float(duration[:-1]) * 1000
    start = end - duration + 1
    return (int(start), int(end))

def solution(lines):
    answer = 0
    arr = []
    for line in lines:
        a, b, c = line.split(" ")
        t = convertSecond(b, c)
        arr.append(t)
    
    arr.sort()
    for a, b in arr:
        cnt1, cnt2 = 0, 0
        for i in range(len(arr)):
            if b <= arr[i][1] and b + 999 >= arr[i][0]:
                cnt1 += 1
            if a - 999 <= arr[i][1] and a >= arr[i][0]:
                cnt2 += 1
                
        answer = max(answer, cnt1)
        answer = max(answer, cnt2)

    return answer
    