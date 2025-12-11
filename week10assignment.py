track_list = [
    "Taylor Swift-Shake it Off-240",
    "Queen-Bohemian Rhapsody-355",
    "Taylor Swift-Love Story-235",
    "Drake-God's Plan-200",
    "Queen-We Will Rock You-120",
    "Drake-Hotline Bling-260"
]
def categorize_music(track_list):
    music_dic= {}
    for item in track_list:
        artist, songname, seconds_str = item.split("-")
        seconds = float(seconds_str)
        if artist not in music_dic:
            music_dic[artist] = []

        music_dic[artist].append((songname,seconds))

    return music_dic

def report_artist_time(music_dict):
    dict = {}
    for artist, songs in music_dict.items():
        print(songs, "\n\n")
        total_time = 0
        for song_name, duration in songs:
            total_time += duration
        dict[artist] = total_time
    for key, value in dict.items():
        print(f"{key}: {value} seconds total")
categorize_music(track_list)
report_artist_time(categorize_music(track_list))
