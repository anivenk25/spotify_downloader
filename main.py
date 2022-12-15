import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
from datetime import datetime
from threading import Thread
from pytube import YouTube


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
playlist_link = str(input('Input Playlist Link : '))
results = sp.playlist_items(playlist_link, None, 100, 0, None, ('track', ))
albums = results['items']

a1=[]

for idx, item in enumerate(results['items']):
    track = item['track']
    a= str(track['artists'][0]['name'])
    b= str(track['name'])
    a1.append(( a, " – ", b))
    print(idx, a, " – ", b)



## google search *****************
start = datetime.now()

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

results = []

# to search
for i in range (0,len(a1)) :
    query = "youtube "+ str(a1[i])
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        print(j)
        if 'youtube' in j :
            results.append(j)
print(results)
print('*****************',len(results),'*****************')
end = datetime.now()

td = (end - start).total_seconds() * 10**3
print(f"The time of execution is : {td:.03f}ms")

# youtube download *****************

def download():
    #start = datetime.now(
        yt = YouTube(results[_])
        yt.streams.get_audio_only('mp4').download()
        #print(_, "****", yt.streams.get_audio_only('mp4'))
    #end = datetime.now()
    #td = (end - start).total_seconds() * 10 ** 3
    #print(f"The time of execution of above program is : {td:.03f}ms")

#threading
tcount=len(results)
for _ in range (tcount):
    t= Thread (
        target=download,
        )
    t.start()