from django.test import TestCase
from django.forms.models import model_to_dict
from .models import Link

class LinkModelTestCase(TestCase):
    def test_only_url_is_needed(self):
        l = Link.objects.create(url='https://google.com')
        l.save()
        self.assertTrue(Link.objects.filter(url='https://google.com').exists())

    def test_id_is_22_characters_long(self):
        l = Link.objects.create(url='https://google.com')
        self.assertEqual(len(l.id), 22)