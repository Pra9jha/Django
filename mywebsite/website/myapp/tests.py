from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
class mytest(TestCase):
      p=Post.objects.all()
      for i in p:
          print("Title is :"+i.title)
          print("Content is :"+i.content)
          print("Posted date is :"+ str(i.date_Posted))
          print("Author is :"+str(i.author))
          print("______________________________________")

      # def adddata(self):
      post_x=Post(title=str(input("Enter the title")),content=str(input("Enter the content")),author=User.objects.all().first())
      post_x.save()
      print(post_x)



