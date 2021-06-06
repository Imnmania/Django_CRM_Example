from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def home_page(request):
    # return HttpResponse('Hello Warudo!')
    leads = Lead.objects.all()
    context = {
        "leads": leads
        # "name": "Joe",
        # "age": 26
    }
    return render(request, "second_page.html", context)