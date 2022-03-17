import yt_dlp
import sys
import os
def download(video_url, isList, path):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )    
    ### todo ###
    # if path doesn't exist, create it

    ratelimit = 5000000
    format = 'bestaudio/mp3'

    # Download all videos in a playlist
    if video_url.startswith('https://www.youtube.com/playlist'):
        ydl_opts = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':  'Downloads/' + '%(title)s.mp3',

        }

    # Download single video from url
    elif video_url.startswith((
        'https://www.youtube.com/watch', 
        'https://www.twitch.tv/', 
        'https://clips.twitch.tv/')):
        ydl_opts = {
            'ignoreerrors': True,
            'abort_on_unavailable_fragments': True,
            'format': format,
            'outtmpl': path + '%(title)s.mp3',
            'ratelimit': ratelimit,
            'keepvideo':False,

        }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_info['webpage_url']])
    if isList:
        with open('list.txt', 'w') as write:
                    write.write('')
def __init__():
    isList = False
    url = ''
    path = 'Downloads/'
    if len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            isList = True
            with open('list.txt', 'r') as read:
                
                while line := read.readline():
                    url = line
                    download(url, isList, path)
                    print('\nDownloading: ', url)
                
            with open('list.txt', 'w') as write:
                write.write('')
            return
        elif sys.argv[1].startswith(('https://www.youtube.com/watch', 
        'https://www.twitch.tv/', 
        'https://clips.twitch.tv/')) or sys.argv[1].startswith('https://www.youtube.com/playlist'):
            url = sys.argv[1]
            isList = False
    else:
        print("\nUrl (press ENTER if downloading from list file): ", end='')
        url = input()
        print("\nLocation: ", end='')
        path = input()
        
        if url == '':
            isList = True
            with open('list.txt', 'r') as read:
                
                while line := read.readline():
                    url = line
                    download(url, isList, path)
                    print('\nDownloading: ', url)
            return
    download(url, isList, path)
__init__()