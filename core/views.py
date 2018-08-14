from django.views.generic.list import ListView
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
import subprocess
from .tasks import download_mpd
from .models import DownloadedVideos
# Create your views here.
def index(request):
	if request.method == 'POST':
		url = request.POST['url']
		print ("request received  " + request.POST['url'])
		try:
			download_mpd.delay(url)
			messages.success(request, 'Your video has been added in the queue!')

		except Exception as e:
			print (e)
			return redirect('error')

	return render(request, 'index.html')

class QueueListView(ListView):
	print (settings.MEDIA_ROOT)
	print (settings.MEDIA_URL)
	model = DownloadedVideos	

	def get_template_names(self):
		return "downloadedvideos_list.html"