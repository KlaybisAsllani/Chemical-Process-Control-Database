from django.test import TestCase
from .models import Reactor

class ReactorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Reactor.objects.create(name='Test Reactor', description='A test reactor', benefits='Test benefits', uses='Test uses', reactor_type='CSTR')

    def test_name_label(self):
        reactor = Reactor.objects.get(id=1)
        field_label = reactor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_description_label(self):
        reactor = Reactor.objects.get(id=1)
        field_label = reactor._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_benefits_label(self):
        reactor = Reactor.objects.get(id=1)
        field_label = reactor._meta.get_field('benefits').verbose_name
        self.assertEqual(field_label, 'benefits')

    def test_uses_label(self):
        reactor = Reactor.objects.get(id=1)
        field_label = reactor._meta.get_field('uses').verbose_name
        self.assertEqual(field_label, 'uses')

    def test_reactor_type_label(self):
        reactor = Reactor.objects.get(id=1)
        field_label = reactor._meta.get_field('reactor_type').verbose_name
        self.assertEqual(field_label, 'reactor type')