import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("one", 4)

    def test_room_has_number(self):
        self.assertEqual("one", self.room.room_number)