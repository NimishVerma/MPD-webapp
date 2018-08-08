from celery.decorators import task
from celery.utils.log import get_task_logger




logger = get_task_logger(__name__)
import youtube_dl


@task(name="download video")
def download_mpd(url):
	with youtube_dl.YoutubeDL({}) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_url = info_dict.get("url", None)
		video_id = info_dict.get("id", None)
		video_title = info_dict.get('title', None)


	ydl_opts = {
	    'format': 'bestvideo+bestaudio/best',
	    'outtmpl': 'media'+/video_id+'%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])