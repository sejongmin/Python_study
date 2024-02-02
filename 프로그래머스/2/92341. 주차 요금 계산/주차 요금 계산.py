def convertMinute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    answer = []
    park = {}
    total = {}
    for record in records:
        time, number, inout = record.split(" ")
        if inout == "IN":
            park[number] = convertMinute(time)
        elif inout == "OUT":
            if number not in total.keys():
                total[number] = 0
            total[number] += convertMinute(time) - park[number]
            park.pop(number)
        
    for key, value in park.items():
        if key not in total.keys():
            total[key] = 0
        total[key] += convertMinute("23:59") - value
    
    total = dict(sorted(total.items()))
    for value in total.values():
        if fees[0] >= value:
            answer.append(fees[1])
        elif fees[0] < value:
            answer.append(fees[1] + (value - fees[0] + fees[2] - 1) // fees[2] * fees[3])
        
    return answer