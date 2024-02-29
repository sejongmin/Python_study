def isTransfer(time, a, b, g, s, w, t):
    sumGS = 0
    sumG = 0
    sumS = 0
    
    for i in range(len(t)):
        count = (time - t[i]) // (2 * t[i]) + 1 if time > t[i] else 0
        total = count * w[i]
        sumGS += min(g[i] + s[i], total)
        sumG += min(g[i], total)
        sumS += min(s[i], total)
    
    if a + b <= sumGS and a <= sumG and b <= sumS:
        return True
    return False
        
def solution(a, b, g, s, w, t):
    left, right = 0, 4*10e14
    while left < right:
        mid = (left + right) // 2
        if isTransfer(mid, a, b, g, s, w, t):
            right = mid
        else:
            left = mid + 1
    
    return left