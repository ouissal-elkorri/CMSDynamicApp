import youtubeScraping
#import  get_playlist_infos


selected_chaine_youtube = 'https://www.youtube.com/c/ButtonPoetry/videos'
selected_play_list_youtube = 'https://www.youtube.com/c/ButtonPoetry/playlists'

print("Chaine : ", selected_chaine_youtube)
for element in youtubeScraping.get_youtube_videos_list(selected_chaine_youtube):
    print(element)
    """for items in get_playlist_infos.get_youtube_videos_playlist(our_link):
        print(items)"""
