class Guest:

    def __init__(self, name, wallet, fav_song, fav_artist):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song
        self.fav_artist = fav_artist

    def pay_entry(self, entry_amount):
        self.wallet -= entry_amount

    def cheer_for_favourite_song(self, song):
        if song.song_name == self.fav_song and song.song_artist == self.fav_artist:
            return "This is my favourite song, yeehaw"
        