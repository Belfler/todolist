import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


class TestNewVisitor(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        self.browser.get('http://localhost:8000')

    def test_start_list_and_retrieve_it_later(self):
        self.assertIn('To-Do List', self.browser.title)

        header = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do List', header)

        input_box = self.browser.find_element_by_id('add-item')
        self.assertEqual('Write new to-do item', input_box.get_attribute('placeholder'))

        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('to-do-list')
        row = table.find_element_by_tag_name('tr')
        self.assertTrue(row.text == '1: Buy milk')
