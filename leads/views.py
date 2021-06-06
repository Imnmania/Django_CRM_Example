from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


def lead_list(request):
    # return HttpResponse('Hello Warudo!')
    leads = Lead.objects.all()
    context = {
        "leads": leads
        # "name": "Joe",
        # "age": 26
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id = pk)
    print(lead)
    return HttpResponse("Here is the detailed view")