from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name='home_page'),
    # path('about/',views.about,name='about_page')
    path('', views.registration, name='register_page'),

    ]


# prabhat
# prab@cmi