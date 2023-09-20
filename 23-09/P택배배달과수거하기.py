def solution(cap, n, deliveries, pickups):
    answer = 0
    
    di = n - 1
    pi = n - 1
    
    while di > -1 and deliveries[di] == 0:
        di -= 1
    while pi > -1 and pickups[pi] == 0:
        pi -= 1
    
    while di > -1 or pi > -1:
        answer += (max(di, pi) + 1) * 2
        d_now = cap
        for j in range(di, -1, -1):
            if j > 0 and deliveries[j] == 0:
                continue
            elif j == 0 and deliveries[j] == 0:
                di = -1
                break
            else:
                if d_now >= deliveries[j]:
                    d_now -= deliveries[j]
                    deliveries[j] = 0
                    if j == 0:
                        di = -1
                else:
                    deliveries[j] -= d_now
                    di = j
                    break

        p_now = 0
        for j in range(pi, -1, -1):
            if j > 0 and pickups[j] == 0:
                continue
            elif j == 0 and pickups[j] == 0:
                pi = -1
                break
            else:
                if (cap - p_now) >= pickups[j]:
                    p_now += pickups[j]
                    pickups[j] = 0
                    if j == 0:
                        pi = -1
                else:
                    pickups[j] -= (cap - p_now)
                    pi = j
                    break
            
    return answer