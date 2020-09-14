import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(1, 10)
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

    def test_adding_to_full_room(self):
        for _ in range(10):                                             # tried just setting the room count to 10 but it wouldn't work for whatever reason so here we are
            self.room.add_guest(self.guest)
        self.assertEqual("Room full.", self.room.add_guest(self.guest))

    def test_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, len(self.room.songs))

    def test_remove_song(self):
        self.room.add_song(self.song)
        self.room.remove_song(self.song)
        self.assertEqual(0, len(self.room.songs))
    
    def test_play_song_and_remove(self):
        self.room.add_song(self.song)
        self.assertEqual("Now playing My Favourite Song by My Favourite Artist", self.room.play_song())


    def test_add_to_tab(self):
        self.room.add_to_tab(10.00)
        self.assertEqual(10.00, self.room.tab)


