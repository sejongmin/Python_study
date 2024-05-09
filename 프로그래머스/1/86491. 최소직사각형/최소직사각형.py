def solution(sizes):
    sizes = list(map(sorted, sizes))
    mh, mv = 0, 0
    for h, v in sizes:
        mh = max(mh, h)
        mv = max(mv, v)
    
    return mh * mv