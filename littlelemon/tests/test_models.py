from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
  def setUp(self):
    Menu.objects.create(Title="IceCream", Price=80, Inventory=100)

  def test_get_item(self):
    item = str(Menu.objects.get(Title="IceCream"))
    self.assertEqual(item, "IceCream : 80.00")