# https://itholic.github.io/kata-best-album/
# 다른 사람 코드, 다시 

from collections import defaultdict
from operator import itemgetter

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

dictGenres = defaultdict(lambda: 0)

for genre, play in zip(genres, plays):
    dictGenres[genre] += play

dictGenres = sorted(dictGenres.items(), key=(lambda x: x[1]), reverse=True)

sortedGenres = [genre for genre, play in dictGenres]

final_dict = defaultdict(lambda: [])
for i, genre_play_tuple in enumerate(zip(genres, plays)):
    final_dict[genre_play_tuple[0]].append((genre_play_tuple[1], i))

answer = []
for genre in sortedGenres:
    one_genre_list = sorted(final_dict[genre], key=(lambda x: x[0]), reverse=True)
    if len(one_genre_list) > 1:
        answer.append(one_genre_list[0][1])
        answer.append(one_genre_list[1][1])
    else:
        answer.append(one_genre_list[0][1])
