from django.test import TestCase, override_settings
from django.urls import reverse


class MaintenanceModeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.home_url = reverse('products:homepage')

    @override_settings(MAINTENANCE_MODE=False)
    def test_maintenance_mode_off(self):
        response = self.client.get(self.home_url)

        self.assertContains(response, 'Welcome to our store', status_code=200)

    @override_settings(MAINTENANCE_MODE=True)
    def test_maintenance_mode_on(self):
        response = self.client.get(self.home_url)

        self.assertContains(response, 'Site under maintenance', status_code=503)
