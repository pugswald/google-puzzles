from r_calc import std2rpn
from unittest import TestCase

class TestRCalc(TestCase):
    
    def goog_test(self):
        self.assertEqual("232*+", std2rpn("2+3*2"))
        self.assertEqual("243**93*5++", std2rpn("2*4*3+9*3+5"))