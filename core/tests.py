from django.test import TestCase, Client
from django.urls import resolve

from core.views import IndexView


class TestIndexPage(TestCase):
    def test_word_django_is_in_title(self):
        client = Client()
        response = client.get('/')
        content = response.content.decode('utf-8')
        self.assertIn('Index page', content)

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, IndexView.as_view().__name__)
