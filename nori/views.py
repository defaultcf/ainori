from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Nori, Kyoten, Comment

# Create your views here.
def index(request):
    latest_nori_list = Nori.objects.order_by('date')
    context = {
        'latest_nori_list': latest_nori_list,
    }
    return render(request, 'nori/index.html', context)

def create(request):
    return render(request, 'nori/create.html')

def created(request):
    try:
        departure = Kyoten.objects.get(area=request.POST['departure'])
        arrival = Kyoten.objects.get(area=request.POST['arrival'])
    except Kyoten.DoesNotExist:
        raise Http404("出発地・到着地のいずれか、もしくは両方が正しく指定されていません")

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
        raise Http404("このidでは存在しません...")

    latest_nori_comment = Comment.objects.all()

    context = {
        'nori': nori,
        'latest_nori_comment': latest_nori_comment,
    }
    return render(request, 'nori/detail.html', context)

def send(request, nori_id):
    try:
        nori = Nori.objects.get(pk=nori_id)
    except Nori.DoesNotExist:
        raise Http404("このidでは存在しません...")

    comment = Comment(
        nori=nori,
        user=request.user,
        comment=request.POST['comment'],
    )
    comment.save()
    return HttpResponse(request.POST['comment'])
