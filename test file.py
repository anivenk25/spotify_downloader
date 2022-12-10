import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
from threading import Thread
from datetime import datetime

# youtube download *****************
def youtube_download1() :
    for m in x[0]:
        from pytube import YouTube

        yt = YouTube(m)
        yt.streams.get_audio_only('mp4').download()
        print(results.index(m), "****", yt.streams.get_audio_only('mp4'))

def youtube_download2() :
    for m in x[1]:
        from pytube import YouTube

        yt = YouTube(m)
        yt.streams.get_audio_only('mp4').download()
        print(results.index(m), "****", yt.streams.get_audio_only('mp4'))

def youtube_download3() :
    for m in x[2]:
        from pytube import YouTube

        yt = YouTube(m)
        yt.streams.get_audio_only('mp4').download()
        print(results.index(m), "****", yt.streams.get_audio_only('mp4'))

def youtube_download4() :
    for m in x[3]:
        from pytube import YouTube

        yt = YouTube(m)
        yt.streams.get_audio_only('mp4').download()
        print(results.index(m), "****", yt.streams.get_audio_only('mp4'))

def youtube_download5() :
    for m in x[4]:
        from pytube import YouTube

        yt = YouTube(m)
        yt.streams.get_audio_only('mp4').download()
        print(results.index(m), "****", yt.streams.get_audio_only('mp4'))


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
playlist_link = str(input('Input Playlist Link : '))
results = sp.playlist_items(playlist_link, None, 100, 0, None, ('track', ))
albums = results['items']

a1=[]

for idx, item in enumerate(results['items']):
    track = item['track']
    a1.append((idx, track['artists'][0]['name'], " – ", track['name']))
    print(idx, track['artists'][0]['name'], " – ", track['name'])



## google search *****************
start = datetime.now()

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

results = []

# to search
for i in range (0,len(a1)) :
    query = str(a1[i]) + 'youtube'
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        print(j)
        if 'youtube' in j :
            results.append(j)
print(results)
print('*****************',len(results),'*****************')
end = datetime.now()

td = (end - start).total_seconds() * 10**3
print(f"The time of execution is : {td:.03f}ms")

#split list ************
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
if len(results)%5==0 :
    n = len(results) // 5
else :
    n = len(results)//5 + 1
x = list(divide_chunks(results, n ))
print(x)




#threading
tcount=5
t1 = Thread (target=youtube_download1)
t2 = Thread (target=youtube_download2)
t3 = Thread (target=youtube_download3)
t4 = Thread (target=youtube_download4)
t5 = Thread (target=youtube_download5)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
