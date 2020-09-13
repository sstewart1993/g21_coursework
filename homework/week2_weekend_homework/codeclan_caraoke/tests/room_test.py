import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(1)
        self.guest = Guest("Cam", 100.00, "My Favourite Song", "My Favourite Artist")
        self.song = Song("My Favourite Song", "My Favourite Artist")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.number)

    def test_room_starts_empty(self):
        self.room.count_guests
        self.assertEqual(0, len(self.room.guests))

    def test_room_starts_with_no_songs(self):
        self.room.count_songs
        self.assertEqual(0, len(self.room.songs))

    def test_tab_starts_zero(self):
        self.assertEqual(0.00, self.room.tab)

    def test_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_remove_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))

    def test_remove_song(self):
        self.room.add_song(self.song)
        self.room.remove_song(self.song)
        self.assertEqual(0, len(self.room.songs))

    
        



        

