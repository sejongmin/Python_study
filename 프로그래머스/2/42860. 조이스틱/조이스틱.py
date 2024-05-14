def solution(name):
    answer = 0
    loc = 0
    tmp = len(name) - 1
    for i in range(len(name)):
        if name[i] != 'A':
            answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            if i == 0: 
                continue
            tmp = min(tmp, min(2 * (len(name) - i) + loc, 2 * loc + len(name) - i))
            loc = i

    answer += min(tmp, loc)
            
    return answer