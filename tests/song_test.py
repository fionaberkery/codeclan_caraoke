import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("The Chain", "Fleetwood Mac")
        self.song2 = Song("Shake It Off", "Taylor Swift")
        self.song3 = Song("Flying Without Wings", "Westlife")
        self.song4 = Song("Simply The Best", "Tina Turner")
        self.song5 = Song("Angel Eyes", "Abba")
        # self.song6 = Song()
        # self.song7 = Song()
        # self.song8 = Song()
        # self.song9 = Song()
        # self.song10 = Song()
        # self.song11 = Song()
        # self.song12 = Song()
        # self.song13 = Song()
        # self.song14 = Song()
        # self.song15 = Song()

    def test_song_has_title(self):
        self.assertEqual("The Chain", self.song1.title)
        self.assertEqual("Simply The Best", self.song4.title)
        self.assertEqual("Angel Eyes", self.song5.title)

    def test_song_has_artist(self):
        self.assertEqual("Taylor Swift", self.song2.artist)
        self.assertEqual("Westlife", self.song3.artist)
        self.assertEqual("Fleetwood Mac", self.song1.artist)