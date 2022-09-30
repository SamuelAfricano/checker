from django.shortcuts import render
from django.http import HttpResponse

from pychecker.utils.connecto import verifica_status_do_site

def index(request):
	status = None
	url = None
	if request.method == 'POST':
		url = request.POST['url']
		status_do_site = verifica_status_do_site(url)
		if status_do_site:
			status = 'online'
		else:
			status = False

	return render(request, "index.html",{"status": status, "site": url})


