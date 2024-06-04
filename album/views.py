from django.shortcuts import render,redirect
from . import forms
from . import models

def add_album(request):
    if request.method =='POST':
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form=forms.AlbumForm()
    return render(request, 'add_album.html',{'form':album_form})

def edit_album(request,id):
    post=models.AlbumModel.objects.get(pk=id)
    album_form=forms.AlbumForm(instance=post)
    if request.method =='POST':
        album_form=forms.AlbumForm(request.POST,instance=post)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'add_album.html',{'form':album_form})

def delete_album(request,id):
    post=models.AlbumModel.objects.get(pk=id)
    post.delete()
    return redirect('home')
