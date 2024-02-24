def solution(begin, target, words):
    answer = 50
    visit = []
    q = []
    q.append((begin, 0))
    visit.append(begin)
    while q:
        s, cnt = q.pop()
        for word in words:
            if word in visit:
                    continue
            xcnt = 0
            for i in range(len(word)):
                if s[i] != word[i]:
                    xcnt += 1
            
            if xcnt == 1:
                if word == target:
                    return cnt + 1
                q.append((word, cnt + 1))
                visit.append(word)
                
    return 0