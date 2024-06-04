

from django.shortcuts import render
from musician.models import MusicianModel

def home(request):
    data = MusicianModel.objects.all().prefetch_related('albums')
    for d in data:
        print(d)
    return render(request, 'index.html', {'data': data})
