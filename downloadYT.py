from pytube import YouTube
import os
# working code and able to Download one video 
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("../")
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
# chande_dir = input("Enter dir name")
# if not os.path.exists(chande_dir):
#     os.mkdir(chande_dir)
#     os.chdir(chande_dir)
# else:
#     os.chdir(chande_dir)
Download(link)