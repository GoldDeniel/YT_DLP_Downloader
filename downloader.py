import yt_dlp
import sys
def download(video_url):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    #filename = f"{video_info['title']}.mp3"
    print("\nLocation:")
    path = input()
    #path = 'Downloads/'

    ratelimit = 5000000
    format = 'bestaudio/mp3'

    # Download all videos in a playlist
    if url.startswith('https://www.youtube.com/playlist'):
        ydl_opts = {
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':  'Downloads/' + '%(title)s.mp3',

        }

    # Download single video from url
    elif url.startswith((
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

    #print("Download complete... {}".format(filename))

if __name__=='__main__':
    if len(sys.argv[1]):
        if sys.argv[1].startswith(('https://www.youtube.com/watch', 
        'https://www.twitch.tv/', 
        'https://clips.twitch.tv/')) or sys.argv[1].startswith('https://www.youtube.com/playlist'):
            url = sys.argv[1]
        else:
            url = input()

    download(url)