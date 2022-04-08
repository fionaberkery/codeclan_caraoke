import unittest

from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("One", 4)
        self.room2 = Room("Two", 8)
        self.room3 = Room("Three", 10)
        self.guest1 = Guest("Fiona", 35)
        self.guest2 = Guest("Debbie", 33)
        self.guest3 = Guest("Heather", 37)
        self.guest4 = Guest("Claire", 31)
        self.guest5 = Guest("Ben", 37)
        self.guest6 = Guest("Dan", 34)
        self.guest7 = Guest("Rob", 30)
        self.guest8 = Guest("Chris", 34)
        self.song1 = Song("The Chain", "Fleetwood Mac")
        self.song2 = Song("Shake It Off", "Taylor Swift")
        self.song3 = Song("Flying Without Wings", "Westlife")
        self.song4 = Song("Simply The Best", "Tina Turner")
        self.song5 = Song("Angel Eyes", "Abba")
        self.song6 = Song("Rock DJ", "Robbie Williams")
        self.song7 = Song("Horses", "Daryl Braithwaite")
        self.song8 = Song("Ashes", "Embrace")
        self.song9 = Song("Sweet Caroline", "Neil Diamond")
        self.song10 = Song("Wonderwall", "Oasis")


    def test_room_has_number(self):
        self.assertEqual("One", self.room1.room_number)

    def test_room_has_a_max_capacity(self):
        self.assertEqual(4, self.room1.max_capacity)
        self.assertEqual(8, self.room2.max_capacity)
        self.assertEqual(10, self.room3.max_capacity)

    def test_room_has_an_empty_guest_list(self):
        self.room1.guest_list_count()
        self.assertEqual(0, self.room1.guest_list_count())

    def test_can_add_guest_to_room(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.guest_list_count())

    def test_can_remove_guest_from_room(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, self.room1.guest_list_count())

    def test_room_has_song_list(self):
        self.room1.song_list_count()
        self.assertEqual(0, self.room1.song_list_count())

    def test_can_room_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, self.room1.song_list_count())

    def test_what_happens_if_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest4)
        self.room1.check_in_guest(self.guest5)
        self.assertEqual("Sorry no more room", self.room1.check_in_guest(self.guest5))