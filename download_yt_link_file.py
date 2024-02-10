from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        print(f"starting download link: {link}")
        youtubeObject.download("../")
    except:
        print("An error has occurred")
    print("Download is completed successfully")

with open('videos_links.txt', 'r') as my_file:
    for line in my_file:
        Download(line)