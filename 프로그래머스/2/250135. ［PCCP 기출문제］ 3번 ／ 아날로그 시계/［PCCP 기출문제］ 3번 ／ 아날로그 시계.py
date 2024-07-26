def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    c = 43200
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    hd1 = h1 % 12 * 3600 + m1 * 60 + s1
    md1 = m1 * 720 + s1 * 12
    sd1 = s1 * 720
    if hd1 == 0 and md1 == 0 and sd1 == 0:
        answer += 1
        
    while start < end:
        hd2 = hd1 + 1
        md2 = md1 + 12
        sd2 = sd1 + 720
        
        if hd2 >= c and md2 >= c and sd2 >= c:
            answer += 1
        else:
            if sd1 < hd1 and sd2 >= hd2:
                answer += 1
            if sd1 < md1 and sd2 >= md2:
                answer += 1
        
        hd1 = hd2 % c
        md1 = md2 % c
        sd1 = sd2 % c
        start += 1
    
    return answer
            
                    
                
                    
        
    