from django.shortcuts import render
from django.http import HttpResponse

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'yout searched for: %s' % request.GET['q']
	else:
		message = 'yout submitted an empty form'
	return HttpResponse(message)