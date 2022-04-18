from itertools import product
import unittest
from products import Item


class ItemTest(unittest.TestCase):
    """Test cases for setting product item attributes"""
 
    def test_tax_with_integer_category(self):     
        item = Item(25,3,'primary')
        item.set_tax()
        self.assertEqual(item.item_tax,0.75)
        item.set_deposit_tax()
        self.assertEqual(item.deposit_tax,0.75)
        item.set_category()
        self.assertEqual(item.primary_tax,0.75)
        item = Item(0.1,0,'luxury')
        self.assertEqual(item.luxury_tax,0)

    def test_tax_with_zeros_categories(self):
        item = Item(0,0,'primary')
        item.set_tax()
        self.assertEqual(item.item_tax,0)
        item.set_deposit_tax()
        self.assertEqual(item.deposit_tax,0)
        item.set_category()
        self.assertEqual(item.primary_tax,0)
        item = Item(0.1,0,'luxury')
        self.assertEqual(item.luxury_tax,0)

    def test_tax_with_invalid_categories(self):
        item = Item(0,0,'primarys')
        item.set_tax()
        self.assertEqual(item.item_tax,0)
        item.set_deposit_tax()
        self.assertEqual(item.deposit_tax,0)
        item.set_category()
        self.assertEqual(item.primary_tax,0)
        item = Item(0.1,0,'luxurys')
        self.assertEqual(item.luxury_tax,0)
        item = Item(25,3,'test')
        item.set_tax()
        self.assertEqual(item.item_tax,0.75)
        item.set_deposit_tax()
        self.assertEqual(item.deposit_tax,0.75)
        item.set_category()
        self.assertEqual(item.primary_tax,0)
        item = Item(0.1,0,'luxurys')
        self.assertEqual(item.luxury_tax,0)
  
if __name__ == '__main__':
    unittest.main()
