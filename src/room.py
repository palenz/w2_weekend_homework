from src.guest import Guest

class Room:

    def __init__(self, room_name, room_song):
        self.room_name = room_name
        self.room_song = room_song
        self.room_guests = []

    def check_in_guest(self, guest):
        self.room_guests.append(guest)

    def check_out_guest(self, guest):
        self.room_guests.remove(guest)