# from django.test import TestCase
# from django.contrib.auth.models import User
# from django.template.loader import render_to_string
#
# class LogInTest(TestCase):
#
#     print("User registered is ")
#     for i in User.objects.all():
#         print(i)
#     def setUp(self):
#         self.credentials = {
#             'username': 'prashant',
#             'password': 'asedrfweggy'}
#         print("Register Test Case is running \n")
#         User.objects.create_user(**self.credentials)
#
#     def test_login(self):
#         response = self.client.post('/login/', self.credentials, follow=True)
#         self.assertTrue(response.context['user'].is_active)
#         print("Login Test Case is running \n")
#
#     def test_logout(self):
#         response = self.client.get('/logout/')
#         print("Log out Test Case is running \n")