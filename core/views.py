from django.shortcuts import render, redirect
from django.http import HttpResponse
import subprocess
from .tasks import download_mpd
# Create your views here.
def index(request):
	if request.method == 'POST':
		url = request.POST['url']
		print ("request received  " + request.POST['url'])
		try:
			download_mpd.delay(url)
		except:
			return redirect('error')

	return render(request, 'index.html')