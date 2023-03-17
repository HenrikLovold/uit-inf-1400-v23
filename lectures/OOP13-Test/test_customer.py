# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:47:47 2023

@author: Rune
"""

import customer
import unittest

class Test_customer(unittest.TestCase):
    
    def setUp(self):
        self._kunde=customer.Customer("Ola")
        self._kunden=customer.Customer("Kari")
        
    def test_constructor(self):
        self.assertEqual(self._kunde.get_name(), "Ola")
        self.assertEqual(self._kunde.get_level(), 1)
        self.assertFalse(self._kunde.is_active())
        self.assertEqual(self._kunde.get_points(), 0)
        
    def test_activation(self):
        self.assertFalse(self._kunde.is_active())
        self._kunde.activation()
        self.assertTrue(self._kunde.is_active())
        
    def test_addpoints(self):
        self._kunde.add_points(10)
        self.assertEqual(self._kunde.get_points(), 10)
        self._kunde.add_points(400)
        self.assertEqual(self._kunde.get_points(),410)
        
    def test_levels(self):
        self._kunden.add_points(10)
        self.assertEqual(self._kunden.get_level(), 1)
        self._kunden.add_points(290)
        self.assertEqual(self._kunden.get_level(), 2)
        self._kunden.add_points(990)
        self.assertEqual(self._kunden.get_level(), 3)
    
if __name__=="__main__":
    unittest.main()