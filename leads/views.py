from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    # return HttpResponse('Hello Warudo!')
    return render(request, "leads/home_page.html")