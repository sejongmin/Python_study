def solution(lottos, win_nums):
    answer = []
    
    zero_cnt = lottos.count(0)
    s_lottos = set(lottos)
    s_win_nums = set(win_nums)
    
    cnt = len(s_lottos | s_win_nums)
    if zero_cnt > 1:
        cnt += zero_cnt - 1
    min_win_cnt = 12 - cnt
    max_win_cnt = min_win_cnt + zero_cnt
    
    answer.append(7 - max_win_cnt if max_win_cnt > 1 else 6)
    answer.append(7 - min_win_cnt if min_win_cnt > 1 else 6)
    
    
    return answer