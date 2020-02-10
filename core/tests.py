from selenium import webdriver
from django.test import TestCase
from django.urls import resolve

from core.views import IndexView


class TestIndexPage(TestCase):
    def test_word_django_is_in_title(self):
        browser = webdriver.Chrome()
        browser.get('http://localhost:8000')
        self.assertIn('Index page', browser.page_source)
        browser.quit()

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func.__name__, IndexView.as_view().__name__)
