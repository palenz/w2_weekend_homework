from src.guest import Guest

class Room:

    def __init__(self, room_name):
        self.room_name = room_name
        self.room_songs = []
        self.room_guests = []

    def check_in_guest(self, guest):
        self.room_guests.append(guest)

    def check_out_guest(self, guest):
        self.room_guests.remove(guest)

    def add_song_to_room(self, song):
        self.room_songs.append(song)