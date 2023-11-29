
from django.urls import path
from first_app import views


urlpatterns = [
    path('',views.Index, name='index'),
    path('form/',views.form,name = 'form')
]