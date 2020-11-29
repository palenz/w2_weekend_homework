from src.guest import Guest

class Room:

    def __init__(self, room_name):
        self.room_name = room_name
        self.room_songs = []
        self.room_guests = []
        self.capacity = 50
        self.fee = 5

    def check_in_guest(self, guest):
        if len(self.room_guests) < self.capacity and guest.cash >= self.fee:
            self.room_guests.append(guest)

    def check_out_guest(self, guest):
        self.room_guests.remove(guest)

    def add_song_to_room(self, song):
        self.room_songs.append(song)
