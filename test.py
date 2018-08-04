# ydl1.py
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://bae.sgp1.digitaloceanspaces.com/videos/61/dash/2c5633104904dba6ba359fb0102b6c5f.mpd'])