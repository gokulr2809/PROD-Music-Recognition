from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path ('',views.index, name='index'),
    path ('history/',views.history, name='history'),
    path('record/',views.rec_func,name='record'),
]
     
