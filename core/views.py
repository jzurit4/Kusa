from django.shortcuts import render, redirect
from .models import Song
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {'songs': songs})

@csrf_protect
def add_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        audio_file = request.FILES.get('audio_file')
        cover_image = request.FILES.get('cover_image')

        if title and artist and audio_file:
            Song.objects.create(
                title=title,
                artist=artist,
                audio_file=audio_file,
                cover_image=cover_image
            )
        return redirect('index')

    return render(request, 'add_song.html')


def add_to_playlist_view(request):
    songs = Song.objects.all()
    return render(request, "addPlaylist.html", {"songs": songs})