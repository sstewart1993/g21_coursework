import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Cam", 100.00, "My Favourite Song", "My Favourite Artist")
        self.song = Song("My Favourite Song", "My Favourite Artist")
        self.room = Room(1, 10)
    
    def test_guest_has_name(self):
        self.assertEqual("Cam", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("My Favourite Song", self.guest.fav_song)

    def test_guest_has_fav_artist(self):
        self.assertEqual("My Favourite Artist", self.guest.fav_artist)

    def test_pay_entry(self):
        self.guest.pay_entry(10.00)
        self.assertEqual(90.00, self.guest.wallet)

    def test_cheer_for_song(self):
        self.room.add_song(self.song)
        self.room.play_song()
        self.assertEqual("This is my favourite song, yeehaw", self.guest.cheer_for_favourite_song(self.song))

   

        
