import unittest

from classes.room import *
from classes.guest import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("One", 6)
        self.room2 = Room("Two", 8)
        self.room3 = Room("Three", 12)
        self.room4 = Room("Four", 15)
        self.room5 = Room("Five", 25)
        self.guest1 = Guest("Fiona", 35)
        self.guest2 = Guest("Debbie", 33)
        self.guest3 = Guest("Heather", 37)
        self.guest4 = Guest("Claire", 31)


    def test_room_has_number(self):
        self.assertEqual("One", self.room1.room_number)

    def test_room_has_a_max_capacity(self):
        self.assertEqual(25, self.room5.max_capacity)
        self.assertEqual(12, self.room3.max_capacity)
        self.assertEqual(8, self.room2.max_capacity)

    def test_room_has_an_empty_guest_list(self):
        self.room1.guest_list_count()
        self.assertEqual(0, self.room1.guest_list_count())

    def test_can_add_guest_to_room(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, self.room1.guest_list_count())