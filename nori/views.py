from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Nori, Kyoten

# Create your views here.
def index(request):
    latest_nori_list = Nori.objects.order_by('date')[:5]
    context = {
        'latest_nori_list': latest_nori_list
    }
    return render(request, 'nori/index.html', context)

def create(request):
    return render(request, 'nori/create.html')

def created(request):
    #msg = request.POST['departure'] + "から" + request.POST['arrival'] + "へ"
    #return HttpResponse(msg)

    departure = get_object_or_404(Kyoten, area=request.POST['departure'])
    arrival = get_object_or_404(Kyoten, area=request.POST['arrival'])

    nori = Nori(
        user=request.user,
        date=request.POST['date'],
        departure=departure,
        arrival=arrival,
        comment=request.POST['comment'],
    )
    nori.save()
    return HttpResponse(request.user.id)

def detail(request, nori_id):
    try:
        nori = Nori.objects.get(pk=nori_id)
    except Nori.DoesNotExist:
        raise Http404("このidでは存在しません。")
    return render(request, 'nori/detail.html', {'nori': nori})

def send(request, nori_id):
    msg = request.POST['comment']
    return HttpResponse(msg)
