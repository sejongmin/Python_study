def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n)]
    
    for a, b in wires:
        tree[a - 1].append(b)
        tree[b - 1].append(a)
    
    for a, b in wires:
        visit1 = []
        visit2 = []
        q1 = []
        q2 = []
        q1.append(a)
        visit1.append(a)
        while q1:
            now = q1.pop(0)
            for e in tree[now - 1]:
                if e not in visit1 and e != b:
                    q1.append(e)
                    visit1.append(e)
                    
        q2.append(b)
        visit2.append(b)
        while q2:
            now = q2.pop(0)
            for e in tree[now - 1]:
                if e not in visit2 and e != a:
                    q2.append(e)
                    visit2.append(e)
                    
        if len(visit1) + len(visit2) == n:
            answer = min(answer, abs(len(visit1) - len(visit2)))
            
    return answer
                    
            
        
        
        
        
        
