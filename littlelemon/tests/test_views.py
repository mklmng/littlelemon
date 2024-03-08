from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
  def setUp(self):
    Menu.objects.create(Title="Cheeseburger", Price=15, Inventory=100)
    Menu.objects.create(Title="Pasta", Price=12, Inventory=10)
    Menu.objects.create(Title="Feta cheese", Price=6, Inventory=20)

  def test_getall(self):
    allItems = Menu.objects.all()
    serializer = MenuSerializer(allItems)
    self.assertTrue(serializer.is_valid)