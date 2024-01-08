from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from first_app.models import *
from django.views import View
from first_app import forms
from django.db.models import Avg


def index(request):
    musician_list = Musician.objects.order_by("First_name")
    dict = {'title' : "Home Page",'musician_list' : musician_list}
    return render(request,'first_app/index.html',context= dict)

def album_list(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_info = Album.objects.filter(artist=artist_id).order_by('name')
    artist_rating = Album.objects.filter(artist=artist_id).aggregate(Avg('rating'))
    dict = {'title' : " Album List",'artist_info':artist_info,'album_inf':album_info,'artist_ratin':artist_rating}
    return render(request,'first_app/album_list.html',context=dict)

def musician_form(request):
    form = forms.MusicianForm()
    if request.method == "POST":
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)


    dict = {'title' : "Musician Form",'musician_form': form}
    return render(request, 'first_app/musician_form.html',context=dict)

def album_form(request):
    form = forms.album_form()
    if request.method == "POST":
        form = forms.album_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    dict = {'title' : "Album Form",'album_form':form}
    return render(request,'first_app/album_form.html',context=dict)

def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == "POST":
        form =forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)
    dict= {'edit_form':form}
    return render(request,'first_app/edit_artist.html',context=dict)


def edit_album(request,album_id):
    album_info = Album.objects.get(pk = album_id)
    form = forms.album_form(instance=album_info)
    dict = {}
    if request.method == "POST":
        form = forms.album_form(request.POST,instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            dict.update({'success_text':"successfully updated!!"})
    dict.update({'edit_form':form})
    dict.update({'album_id':album_id})
    return render(request,'first_app/edit_album.html',context=dict)

def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    dict = {'deleted_mes':"Album deleted Successfully!!"}
    return render(request,'first_app/delete.html',context=dict)


def delete_musician(request,artist_id):
    delete_artist = Musician.objects.get(pk=artist_id).delete()
    dict = {'deleted_mes':"Musician deleted Successfully!!",}
    return render(request,'first_app/delete.html',context=dict)





























# # Create your views here.
# def index(request):
#     #SELECT * from Musician order by first_name
#     # musician_list = Musician.objects.order_by('First_name')
#     dict = {'text_1' :'i m learning django'}
#     return render(request,'first_app/index.html',context=dict)

# def contact(request):
#     return HttpResponse("<h1>this is contact</h1><a href '/'>Homepage</a><a href = '/About/'>About</a>")

# def about(request):
#     return HttpResponse("<h1>this is about page</h1><a href '/'>Homepage</a><a href ='/Contact/'>Contact</a>")

# def form(request):
#     new_form = forms.MusicianForm()

#     if request.method == 'POST':
#         new_form = forms.MusicianForm(request.POST)
#         if new_form.is_valid():
#             new_form.save(commit=True)
#             return index(request)
#     dict = {'user_form':new_form,'head_1':'Add new musician'}
    
#     ## this is for the forms.py sec -1
#     # new_form = forms.user_form()
#     # dict = {'user_form' : new_form,'heading': "this from is created by django"}


#     # if request.method == 'POST':
#     #     new_form = forms.user_form(request.POST)
#     #     dict.update({'user_form' : new_form})
#     #     if new_form.is_valid():
#     #         user_name = new_form.cleaned_data['user_name']
#     #         user_dob = new_form.cleaned_data['user_dob']
#     #         user_email = new_form.cleaned_data['user_email']


#     #         dict.update({'user_name':user_name})
#     #         dict.update({'user_dob' : user_dob})
#     #         dict.update({'user_email': user_email})
#     #         dict.update({'form_submitted' : 'yes'})

#     return render(request, 'first_app/form.html',context=dict)