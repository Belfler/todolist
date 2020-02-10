from django.test import TestCase

from selenium import webdriver


class TestIndexPage(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_word_django_is_in_title(self):
        self.browser.get('http://localhost:8000')
        assert 'Django' in self.browser.title
