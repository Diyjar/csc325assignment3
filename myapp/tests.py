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

class ApiStatusTests(TestCase):
    def test_api_status_returns_json(self):
        response = self.client.get(reverse("api_status"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.json()["status"], "ok")
        self.assertEqual(response.json()["version"], "1.0.0")

    def test_api_status_rejects_post(self):
        response = self.client.post(reverse("api_status"))

        self.assertEqual(response.status_code, 405)

class ApiHealthTests(TestCase):
    def test_api_health_returns_true(self):
        response = self.client.get(reverse("api_health"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"healthy": True})