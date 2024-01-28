import os, re
from pytube import Playlist,YouTube
# working code to downloading all videos from playlist one by one

def dw_playlist(playlist_url):
    playlist = Playlist(playlist_url)

    playlist_name = re.sub(r'\W+', '-', playlist.title)

    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)
        os.chdir(playlist_name)

    print(f'number of videos {len(playlist.video_urls)}')
    for vid_url in playlist.video_urls:
        print(f'video url: {vid_url}')
        youtubeObject = YouTube(vid_url,use_oauth=True)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            os.chdir(playlist_name)
            print(os.getcwd())
            youtubeObject.download()
        except:
            print("An error has occurred")
        print("Download is completed successfully")

link = input("Enter the YouTube video list URL: ")
dw_playlist(link)