from django.test import TestCase
from main.models import *
from main.views import *
from django.http import HttpRequest


class test_login(TestCase):
    def test_can_access_login_page(self):
        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login(self):
        request = HttpRequest()
        response = authenticate(request,username='test',password='test')
        self.assertEqual(response.status_code, 200)
    
    def test_login_success(self):
        user = CustomUser.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        request = HttpRequest()
        response = authenticate(request,username='testuser', password='12345')
        self.assertEqual(response, True)
        test = self.client.post('/auth/login', {'username':'testuser', 'password': '12345'})
        self.assertEqual(test.status_code, 302)