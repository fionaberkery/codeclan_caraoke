import unittest

from classes.guest import Guest 
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Fiona", 50)
        self.guest2 = Guest("Debbie", 60)
        self.guest3 = Guest("Heather", 30)
        self.guest4 = Guest("Claire", 80)
        self.guest5 = Guest("Ben", 40)
        self.guest6 = Guest("Dan", 50)
        self.guest7 = Guest("Rob", 90)
        self.guest8 = Guest("Chris", 20)
        self.guest9 = Guest("Shona", 100)
        self.guest10 = Guest("Fraser", 150)
        self.room1 = Room("Neon Nights", 4, 3)
        self.room2 = Room("Glitter Ball Dreams", 8, 6)
        self.room3 = Room("Space Cave", 10, 8)

    def test_guest_has_name(self):
        self.assertEqual("Fiona", self.guest1.name)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(150, self.guest10.wallet)

    def test_guest_has_money_in_wallet(self):
        self.assertEqual(90, self.guest7.wallet)

    def test_guest_can_afford_entry(self):
        self.assertEqual(True, self.guest1.check_wallet(self.room1.entry_fee))

    def test_can_wallet_amount_reduce(self):
        self.assertEqual(47, self.guest1.remove_money_from_wallet(self.room1.entry_fee))

    def test_pay_room_entry(self):
        self.guest1.check_wallet(self.room1.entry_fee)
        self.guest1.remove_money_from_wallet(self.room1.entry_fee)
        self.room1.add_money(self.room1.entry_fee)