import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Song Name", "Song Artist")

    def test_song_has_name(self):
        self.assertEqual("Song Name", self.song.song_name)

    def test_song_has_artist(self):
        self.assertEqual("Song Artist", self.song.song_artist)