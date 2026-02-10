from django.shortcuts import render

def home(request):
  return render(request, 'home/home.html')

def contact(request):
  return render(request, 'home/contact.html')

def news(request):
  return render(request, 'home/news.html')
