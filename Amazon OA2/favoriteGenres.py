
# Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.
#
# Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.
#
# The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre.
# A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.
# Input:
# userSongs = {
#    "David": ["song1", "song2", "song3", "song4", "song8"],
#    "Emma":  ["song5", "song6", "song7"]
# },
# songGenres = {
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }
#
# Output: {
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }
#
# Explanation:
# David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
# Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
# {"Rock":2,"Techno":2,"Jazz":1}
# {"Pop":2,"Dubstep":1}
def favorite_genres(userSongs,songGenres):
    song_genre_dict = {}
    for genre, songs in songGenres.items():
        for song in songs:
            song_genre_dict[song] = genre

    ans = {}
    for user, songs in userSongs.items():
        genre_count_dict = {}
        maxcount = 0
        for song in songs:
            genre = song_genre_dict.get(song, None)
            if genre != None:
                genre_count_dict[genre] = genre_count_dict.get(genre, 0) + 1
                maxcount = max(maxcount, genre_count_dict[genre])

        genres = []
        for genre, count in genre_count_dict.items():
            if count == maxcount:
                genres.append(genre)

        ans[user] = genres

    return ans
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

print(favorite_genres(userSongs,songGenres))