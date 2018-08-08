from youtube_dl import YoutubeDL
url = 'http://dash.akamaized.net/dash264/CTA/imsc1/IT1-20171027_dash.mpd'
ytdl = YoutubeDL()
info = ytdl.extract_info(url, download=False)

formats = info['formats']

for format in formats:
	print (format)