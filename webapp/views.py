from django.shortcuts import get_object_or_404, render

from .models import Diary

# Create your views here.

def index(request):
    diary_all = Diary.objects.all().order_by('-id')

    return render(request, 'index.html', {"diary_all": diary_all})

def viewmore(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)

    if diary_id == 1:
        context = {"diary": diary,
                "next_id": diary_id + 1,
                "flag": "first"}
    elif diary_id == len(Diary.objects.all()):
        context = {"diary": diary,
                "previous_id": diary_id - 1,
                "flag": "last"}
    else:
        context = {"diary": diary,
                "previous_id": diary_id - 1,
                "next_id": diary_id + 1}

    return render(request, 'view_more.html', context)
