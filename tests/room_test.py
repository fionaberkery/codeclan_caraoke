import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("One", 6)
        self.room2 = Room("Two", 8)
        self.room3 = Room("Three", 12)
        self.room4 = Room("Four", 15)
        self.room5 = Room("Five", 25)


    def test_room_has_number(self):
        self.assertEqual("One", self.room1.room_number)

    def test_room_has_a_max_capacity(self):
        self.assertEqual(25, self.room5.max_capacity)
        self.assertEqual(12, self.room3.max_capacity)
        self.assertEqual(8, self.room2.max_capacity)