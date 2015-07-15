from balance import balance
from unittest import TestCase

class TestBalance(TestCase):
    
    def goog_test(self):
        self.assertEqual(["L", "R"], balance(2))
        self.assertEqual(["L", "-", "R"], balance(8))
        
    def my_test(self):
        self.assertEqual(["L", "L", "R"], balance(5))
        self.assertEqual(["L", "L", "L", "R"], balance(14))
        self.assertEqual(["R", "R", "L", "R"], balance(22))
       
        
        