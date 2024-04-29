def solution(genres, plays):
    answer = []
    total_plays = {}
    music = {genre:[] for genre in set(genres)}
    for i in range(len(genres)):
        total_plays[genres[i]] = total_plays.get(genres[i], 0) + plays[i]
        music[genres[i]].append([i, plays[i]])
    
    rank = sorted(total_plays.items(), key=lambda x:-x[1])
    for genre, total in rank:
        music[genre].sort(key=lambda x:-x[1])
        answer.append(music[genre][0][0])
        if len(music[genre]) > 1:
            answer.append(music[genre][1][0])
    
    return answer
    
        