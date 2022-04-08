import unittest

from classes.guest import Guest 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Fiona", 35)
        self.guest2 = Guest("Debbie", 33)
        self.guest3 = Guest("Heather", 37)
        self.guest4 = Guest("Claire", 31)

    def test_guest_has_name(self):
        self.assertEqual("Fiona", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(33, self.guest2.age)