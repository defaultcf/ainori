from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        msg = "You are login!"
    else:
        msg = "You are not login..."
    return HttpResponse(msg)
