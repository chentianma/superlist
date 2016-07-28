from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found =resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        print(response.content)
        self.assertTrue(response.content.strip().startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))