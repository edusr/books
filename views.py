from django.shortcuts import render
from django.http import HttpResponse
from models import Book,Publisher,Author
from forms import ContactForm, InsertBookForm
from django.core.mail import send_mail

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request,'search_results.html',{'books':books,'query':q})
	return render(request,'search_form.html',{"error":error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),['siteowner@example.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})

def insert_book(request):
    if request.method == 'POST':
        form = InsertBookForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book = Book(title=cd['title'],publisher=Publisher.objects.get(id=cd['publisher']),publication_date=cd['publication_date'])
            book.save();
            authors=Author.objects.get(id=cd['authors'])
            book.authors.add(authors)
            return HttpResponseRedirect('/contact/thanks/')

    else:
        form = InsertBookForm(initial={'title': 'I love your site!'})
    return render(request, 'insert_book.html', {'form': form})