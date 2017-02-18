from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Nori

# Create your views here.
def index(request):
    latest_nori_list = Nori.objects.order_by('date')[:5]
    context = {
        'latest_nori_list': latest_nori_list
    }
    return render(request, 'nori/index.html', context)

def create(request):
    return render(request, 'nori/create.html')

def detail(request, nori_id):
    try:
        nori = Nori.objects.get(pk=nori_id)
    except Nori.DoesNotExist:
        raise Http404("このidでは存在しません。")
    return render(request, 'nori/detail.html', {'nori': nori})

def send(request, nori_id):
    msg = request.POST['comment']
    return HttpResponse(msg)
