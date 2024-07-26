from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    
    def setUp(self):
        Item.objects.create(name="Mleko", quantity=2)
        Item.objects.create(name="Chleb", quantity=1)
    
    def test_item_creation(self):
        mleko = Item.objects.get(name="Mleko")
        chleb = Item.objects.get(name="Chleb")
        self.assertEqual(mleko.name, "Mleko")
        self.assertEqual(mleko.quantity, 2)
        self.assertEqual(chleb.name, "Chleb")
        self.assertEqual(chleb.quantity, 1)
    
    def test_item_str_representation(self):
        item = Item(name="Masło", quantity=3)
        self.assertEqual(str(item), "Masło - 3")



