import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("The Chain", "Fleetwood Mac")

    def test_song_has_title(self):
        self.assertEqual("The Chain", self.song.title)

