import youtube_dl


# @shared_task
def download_mpd(url):
	ydl_opts = {
	    'format': 'bestvideo+bestaudio/best',
	    'outtmpl': 'test.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])