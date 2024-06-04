from django.shortcuts import render,redirect
from . import forms
from . import models

def add_musician(request):
    if request.method =='POST':
        musician_form=forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form=forms.MusicianForm()
    return render(request, 'add_musician.html',{'form':musician_form})

def edit_musician(request,id):
    post=models.MusicianModel.objects.get(pk=id)
    musician_form=forms.MusicianForm(instance=post)
    if request.method =='POST':
        musician_form=forms.MusicianModel(request.POST,instance=post)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    return render(request, 'add_musician.html',{'form':musician_form})
