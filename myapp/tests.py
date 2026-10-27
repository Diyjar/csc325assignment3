from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_returns_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(response, "<h1>Welcome to the Home Page!</h1>", html=True)


class AboutViewTests(TestCase):
    def test_about_page_returns_about_content(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(
            response,
            "<h1>About Us</h1><p>This is the about page.</p>",
            html=True,
        )
