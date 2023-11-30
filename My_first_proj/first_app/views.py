from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from first_app.models import *
from django.views import View
from first_app import forms

# Create your views here.
def index(request):
    #SELECT * from Musician order by first_name
    musician_list = Musician.objects.order_by('First_name')
    dict = {'text_1' :'i m learning django','musician':musician_list}
    return render(request,'first_app/index.html',context=dict)

def contact(request):
    return HttpResponse("<h1>this is contact</h1><a href '/'>Homepage</a><a href = '/About/'>About</a>")

def about(request):
    return HttpResponse("<h1>this is about page</h1><a href '/'>Homepage</a><a href ='/Contact/'>Contact</a>")

def form(request):
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    dict = {'user_form':new_form,'head_1':'Add new musician'}
    
    ## this is for the forms.py sec -1
    # new_form = forms.user_form()
    # dict = {'user_form' : new_form,'heading': "this from is created by django"}


    # if request.method == 'POST':
    #     new_form = forms.user_form(request.POST)
    #     dict.update({'user_form' : new_form})
    #     if new_form.is_valid():
    #         user_name = new_form.cleaned_data['user_name']
    #         user_dob = new_form.cleaned_data['user_dob']
    #         user_email = new_form.cleaned_data['user_email']


    #         dict.update({'user_name':user_name})
    #         dict.update({'user_dob' : user_dob})
    #         dict.update({'user_email': user_email})
    #         dict.update({'form_submitted' : 'yes'})

    return render(request, 'first_app/form.html',context=dict)