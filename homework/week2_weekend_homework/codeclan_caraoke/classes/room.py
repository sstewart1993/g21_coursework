class Room:
    
    def __init__(self, number):
        self.number = number
        self.guests = []
        self.songs = []
        self.tab = 0.00

    def count_guests(self):
        return len(self.guests)

    def count_songs(self):
        return len(self.songs)

    def add_guest(self, guest):
        self.guests.append(guest)
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)