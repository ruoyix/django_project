from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import urls


class LoginVIewTest(TestCase):
    def test_get(self):
        path = reverse("ruoyi_mall:login")
        response = self.client.get(path)
        template_name = "ruoyi_mall/login.html"
        self.assertTemplateUsed(response, template_name)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        User.objects.create_user(username="ruoyi", password="ruoyi123456")
        path = reverse("ruoyi_mall:login")
        username = "ruoyi"
        password = "ruoyi123456"
        data = {"username": username, "password": password}
        response = self.client.get(path, data)
        expected_url = reverse("ruoyi_mall:index")
        status_code = 302
        target_status_code = 404
        self.assertRedirects(response, expected_url, status_code, target_status_code)

