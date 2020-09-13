class Room:
    
    def __init__(self, number, capacity):
        self.number = number
        self.guests = []
        self.songs = []
        self.capacity = capacity
        self.tab = 0.00

    def count_guests(self):
        return len(self.guests)

    def count_songs(self):
        return len(self.songs)

    def add_guest(self, guest):
        if self.count_guests() < self.capacity:
            self.guests.append(guest)
        else:
            return "Room full."
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def play_song(self):
        next_song = self.songs[0]
        return f"Now playing {next_song.song_name} by {next_song.song_artist}"

    def add_to_tab(self, amount):
        self.tab += amount
