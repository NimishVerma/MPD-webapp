from celery.decorators import task
from celery.utils.log import get_task_logger
from .models import DownloadedVideos
from mysite.settings import PROJECT_ROOT


logger = get_task_logger(__name__)
import youtube_dl


@task(name="download video")
def download_mpd(url):
	with youtube_dl.YoutubeDL({}) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_url = info_dict.get("url", None)
		video_id = info_dict.get("id", None)
		video_title = info_dict.get('title', None)
		ext = info_dict.get('ext', None)


	ydl_opts = {
	    'format': 'bestvideo+bestaudio/best',
	    'outtmpl': 'mysite/media/'+video_id+'.'+ext,
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])
	obj = DownloadedVideos.objects.create()
	print (PROJECT_ROOT)
	obj.path = PROJECT_ROOT+'/media/'+ video_id + '.'+ext
	print (obj.path)
	obj.name = video_id+'.'+ext
	obj.title = video_title
	obj.save()
	print("object saved")