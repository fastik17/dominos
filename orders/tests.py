from collections import OrderedDict
from mixer.backend.django import mixer
from rest_framework.reverse import reverse

from dominos.tests import BaseAPITest
from orders.models import Order


class TestCashierProductViewSet(BaseAPITest):

    def setUp(self):
        self.user = self.create_and_login()

        self.order = mixer.blend(Order)
        self.data = {
            "pizza": [
                {
                    "flavor": "TEXAS",
                    "size": "MEDIUM",
                    "quantity": 1
                },
            ],
            'customer': self.user,
            'customer_address': 'New York',
            'status': 'BOX',
        }

    def test_list_order(self):
        resp = self.client.get(reverse('v1:orders:orders-list'))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)
        self.assertEqual(resp.data['results'][0]['id'], self.order.id)
        self.assertEqual(resp.data['results'][0]['customer'], OrderedDict(resp.data['results'][0]['customer']))
        self.assertEqual(resp.data['results'][0]['customer_address'], self.order.customer_address)
        self.assertEqual(resp.data['results'][0]['status'], self.order.status)

    def test_retrieve_order(self):
        resp = self.client.get(reverse('v1:orders:orders-detail', args=(self.order.id,)))

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['id'], self.order.id)
        self.assertEqual(resp.data['customer'], OrderedDict(resp.data['customer']))
        self.assertEqual(resp.data['customer_address'], self.order.customer_address)
        self.assertEqual(resp.data['status'], self.order.status)

    def test_destroy_order(self):
        resp = self.client.delete(reverse('v1:orders:orders-detail', args=(self.order.id,)))

        self.assertEqual(resp.status_code, 204)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())

    def test_unauthorized(self):
        self.logout()
        resp = self.client.get(reverse('v1:orders:orders-list'))
        self.assertEqual(resp.status_code, 401)
