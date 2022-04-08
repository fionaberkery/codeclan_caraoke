import unittest

from classes.guest import Guest 
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Fiona", 35, 50)
        self.guest2 = Guest("Debbie", 33, 60)
        self.guest3 = Guest("Heather", 37, 30)
        self.guest4 = Guest("Claire", 31, 80)
        self.guest5 = Guest("Ben", 37, 40)
        self.guest6 = Guest("Dan", 34, 50)
        self.guest7 = Guest("Rob", 30, 90)
        self.guest8 = Guest("Chris", 34, 20)
        self.guest9 = Guest("Shona", 65, 100)
        self.guest10 = Guest("Fraser", 68, 150)

    def test_guest_has_name(self):
        self.assertEqual("Fiona", self.guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(33, self.guest2.age)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(150, self.guest10.wallet)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(90, self.guest7.wallet)

    