import unittest

from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Neon Nights", 4, 3)
        self.room2 = Room("Glitter Ball", 8, 6)
        self.room3 = Room("Space Cave", 10, 8)
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
        self.song1 = Song("The Chain", "Fleetwood Mac")
        self.song2 = Song("Shake It Off", "Taylor Swift")
        self.song3 = Song("Purple Rain", "Prince")
        self.song4 = Song("Simply The Best", "Tina Turner")
        self.song5 = Song("Angel Eyes", "Abba")
        self.song6 = Song("Rock DJ", "Robbie Williams")
        self.song7 = Song("Horses", "Daryl Braithwaite")
        self.song8 = Song("Ashes", "Embrace")
        self.song9 = Song("Sweet Caroline", "Neil Diamond")
        self.song10 = Song("Two Of Us", "The Beatles")
        self.song11 = Song("Teenage Dirtbag", "Wheatus")
        self.song12 = Song("I Will Wait", "Mumford & Sons")
        self.song13 = Song("I'd Do Anything For Love", "Meatloaf")
        self.song14 = Song("I Drove All Night", "Celine Dion")
        self.song15 = Song("Everlasting Love", "Love Affair")


    def test_room_has_name(self):
        self.assertEqual("Neon Nights", self.room1.name)

    def test_room_has_a_max_capacity(self):
        self.assertEqual(4, self.room1.max_capacity)
        self.assertEqual(8, self.room2.max_capacity)
        self.assertEqual(10, self.room3.max_capacity)

    def test_room_has_an_empty_guest_list(self):
        self.room1.how_many_guests()
        self.assertEqual(0, self.room1.how_many_guests())

    def test_can_add_guest_to_room(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.how_many_guests())

    def test_can_remove_guest_from_room(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, self.room1.how_many_guests())

    def test_room_has_song_list(self):
        self.room1.how_many_songs()
        self.assertEqual(0, self.room1.how_many_songs())

    def test_can_room_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1, self.room1.how_many_songs())

    def test_what_happens_if_at_capacity(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest2)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest4)
        self.room1.check_in_guest(self.guest5)
        self.assertEqual(1, self.room1.queue_length())

    def test_rooms_entry_fee_amount(self):
        self.assertEqual(6, self.room2.entry_fee)

    def test_till_amount_can_increase(self):
        self.assertEqual(3, self.room1.add_money(self.room1.entry_fee))

    def test_guest_checks_in(self):
        self.guest1.check_wallet(self.room1.entry_fee)
        self.guest1.remove_money_from_wallet(self.room1.entry_fee)
        self.room1.add_money(self.room1.entry_fee)
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.how_many_guests())
