from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import  login_required
from .models import Post
# posts=[
#     {
#         'author':'Prashant Jha',
#         'title':'My Nation',
#         'content':'Will be uploaded .......',
#         'date_posted':'August 27,2018'
#     },
#     {
#         'author':'Prabhat Jha',
#         'title':'Mathematics',
#         'content': 'Will be uploaded .......',
#         'date_posted':'October 28,2018'
#     },
# ]

@login_required
def home(request):
    context={'post':Post.objects.all()}
    return render(request, 'myapp/myapp_home.html',context)


def about(request):
    return render(request, 'myapp/myapp_about.html')


