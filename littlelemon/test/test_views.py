from django.test import TestCase
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    @classmethod
    def setUp(self):
        self.item1 = MenuItem.objects.create(
            id=1,
            title="IceCream", price=80, inventory=10)
        self.item2 = MenuItem.objects.create(
            id=2,
            title="Pizza", price=200, inventory=10)
        self.item3 = MenuItem.objects.create(
            id=3,
            title="Burger", price=100, inventory=10)

    def test_getall(self):
        menus = MenuItem.objects.all()
        menuSerializes = MenuItemSerializer(menus, many=True)
        self.assertEqual(menuSerializes.data, [
                         {'id': 1, 'title': 'IceCream',
                             'price': '80.00', 'inventory': 10},
                         {'id': 2, 'title': 'Pizza',
                             'price': '200.00', 'inventory': 10},
                         {'id': 3, 'title': 'Burger',
                             'price': '100.00', 'inventory': 10}
                         ])
