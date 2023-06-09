from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from .factories import PlaceFactory


class PlacesListTestCase(TestCase):
    def test_open_list_success(self):
        place_1 = PlaceFactory(name='Cool place', description='Visit now!')
        place_2 = PlaceFactory()

        url = reverse('places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        places = response.context.get('places')
        self.assertIsInstance(response.context.get('places'), QuerySet)

        self.assertEqual('Location - 1', places[1].location)
        self.assertEqual(places[0].description, 'Visit now!')


class PlaceCreateTestCase(TestCase):
    def test_create_place_success(self):
        url = reverse('create-place')
        data = {
            'name': 'Kap',
            'location': 'Kochkor region',
            'description': 'Valley in KG'
        }
        response = self.client.post(url, data)
        place = Place.objects.last()
        self.assertEqual(place.name, 'Kap')