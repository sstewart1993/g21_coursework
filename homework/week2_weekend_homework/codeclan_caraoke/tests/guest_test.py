import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Cam", 100.00, "My Favourite Song", "My Favourite Artist")
    
    def test_guest_has_name(self):
        self.assertEqual("Cam", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("My Favourite Song", self.guest.fav_song)

    def test_guest_has_fav_artist(self):
        self.assertEqual("My Favourite Artist", self.guest.fav_artist)

        
