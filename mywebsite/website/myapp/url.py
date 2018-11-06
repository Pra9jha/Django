from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('',views.about,name='about_page')
    ]




# prashant@9