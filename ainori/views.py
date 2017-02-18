from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        msg = "You are login!"
    else:
        msg = "You are not login..."

    context = {
        'msg': msg
    }
    return render(request, 'ainori/index.html', context)
