def solution(genres, plays):
    music_dict = {}
    genre_sum = {}
    result = []
    for i in range(len(genres)):
        music_dict[genres[i]] = music_dict.get(genres[i],[]) + [[i,plays[i]]]
        genre_sum[genres[i]] = genre_sum.get(genres[i],0) + plays[i]
    
    for i in sorted(genre_sum.items(), key = lambda x:x[1], reverse=True):
        for index,value in enumerate(sorted(music_dict[i[0]], key= lambda x: x[1], reverse=True)):
            if index >= 2:
                break
            print(index, value)
            result.append(value[0])

    return result


print(solution(["classic", "pop", "classic", "classic", "pop","pop"],[500, 600, 150, 800, 2500, 200]))