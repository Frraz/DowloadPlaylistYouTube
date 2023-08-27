from pytube import Playlist, YouTube

p = Playlist('link da playlist')
print('Número de vídeos na playlist: %s' % len(p.video_urls))

for i in range(len(p.video_urls)):
    yt = YouTube(p.video_urls[i])
    print('Rwmaning Vídeos: ',len(p.video_urls) - 1)
    print(f'{yt.title} is downloading...')
    yt.streams.filter(adaptive=True)
    stream = yt.streams.get_by_itag(22)
    stream.download()
    