from django.http import request
from django.shortcuts import render
from joke_truy_na.models import Prisoner
# Create your views here.

def homepage_render(request):
    prisoner_list = Prisoner.objects.all()
    context = {
        'prisoner_list': prisoner_list
    }
    return render(request, 'bulletin_board.html', context)

def prisoner_detail(request, pk):
    prisoner_list = Prisoner.objects.get(pk=pk)
    context = {
        "prisoner_list": prisoner_list
    }
    return render(request, 'prisoner_info.html', context)