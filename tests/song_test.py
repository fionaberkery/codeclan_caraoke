import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("The Chain", "Fleetwood Mac")
        self.song2 = Song("Shake It Off", "Taylor Swift")
        self.song3 = Song("Purple Rain", "Prince")
        self.song4 = Song("Simply The Best", "Tina Turner")
        self.song5 = Song("Angel Eyes", "Abba")
        self.song6 = Song("Rock DJ", "Robbie Williams")
        self.song7 = Song("Horses", "Daryl Braithwaite")
        self.song8 = Song("Ashes", "Embrace")
        self.song9 = Song("Sweet Caroline", "Neil Diamond")
        self.song10 = Song("Wonderwall", "Oasis")
        self.song11 = Song("Teenage Dirtbag", "Wheatus")
        self.song12 = Song("I Will Wait", "Mumford & Sons")
        self.song13 = Song("I'd Do Anything For Love", "Meatloaf")
        self.song14 = Song("I Drove All Night", "Celine Dion")
        self.song15 = Song("If I Could Turn Back Time", "Cher")

    def test_song_has_title(self):
        self.assertEqual("The Chain", self.song1.title)
        self.assertEqual("Simply The Best", self.song4.title)
        self.assertEqual("Angel Eyes", self.song5.title)

    def test_song_has_artist(self):
        self.assertEqual("Taylor Swift", self.song2.artist)
        self.assertEqual("Prince", self.song3.artist)
        self.assertEqual("Fleetwood Mac", self.song1.artist)