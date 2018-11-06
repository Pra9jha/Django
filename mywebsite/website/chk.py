from django.contrib.auth.models import User
User.object.all()
User.objects.all()
# <QuerySet [<User: jha>, <User: test_user>]>
# >>> User.objects.all().first()
# <User: jha>
# >>> user=User.objects.all().first()
# >>> user
# <User: jha>
# >>> user.id
# 1
# >>> user.pk
# 1
# >>> user=User.objects.get(id=1)
# >>> user
# <User: jha>
# >>> Post.objects.all()
# <QuerySet []>
# >>> post_1=Post(title='Web development',content='Django content',author=user)
# >>> Post.objects.all()
# <QuerySet []>
# >>> post_1.save()
# >>> Post.objects.all()
# <QuerySet [<Post: Web development>]>
# >>> post_2=Post(title='Mathematics ',content='Mathematical content',author=Prabhat)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Prabhat' is not defined
# >>> post_2=Post(title='Mathematics ',content='Mathematical content',author="Prabhat")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\Prashant Jha\PycharmProjects\django_website\venv\lib\site-packages\django\db\models\base.py", line 467, in __ini
# t__
#     _setattr(self, field.name, rel_obj)
#   File "C:\Users\Prashant Jha\PycharmProjects\django_website\venv\lib\site-packages\django\db\models\fields\related_descriptors.p
# y", line 210, in __set__
#     self.field.remote_field.model._meta.object_name,
# ValueError: Cannot assign "'Prabhat'": "Post.author" must be a "User" instance.
# >>> post_2=Post(title='Mathematics ',content='Mathematical content',author=user)
# >>> Post.objects.all()
# <QuerySet [<Post: Web development>]>
# >>> post_1.save()
# >>> Post.objects.all()
# <QuerySet [<Post: Web development>]>
# >>> post_2.save()
# >>> Post.objects.all()
# <QuerySet [<Post: Web development>, <Post: Mathematics >]>
# >>> post=Post.object.first()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: type object 'Post' has no attribute 'object'
# >>> post=Post.objects.first()
# >>> post.content
# 'Django content'
# >>> post.date_posted
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Post' object has no attribute 'date_posted'
# >>> post.author
# <User: jha>
# >>> post.date_Posted
# datetime.datetime(2018, 11, 4, 11, 54, 53, 501791, tzinfo=<UTC>)
# >>>
