from django.shortcuts import render
from django.http import HttpResponse
from .models import Upload
from .forms import UploadForm


def index(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('done!')

    return render(request, 'index.html', {'data': form})


def display(request):
    return HttpResponse('for image display')
