def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s1, s2, s3 = 0, 0, 0
    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            s1 += 1
        if p2[i % len(p2)] == answers[i]:
            s2 += 1
        if p3[i % len(p3)] == answers[i]:
            s3 += 1
    
    answer = [1, 2, 3]
    m = max(s1, s2)
    m = max(m, s3)
    if m != s1:
        answer.remove(1)
    if m != s2:
        answer.remove(2)
    if m != s3:
        answer.remove(3)
    
    return answer