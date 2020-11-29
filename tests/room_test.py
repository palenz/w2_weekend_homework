import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

# 1. Create rooms

    def test_create_room(self):
        new_room = Room('The Heavy Room')
        self.assertEqual('The Heavy Room', new_room.room_name)

    def test_check_in(self):
        new_guest = Guest('Jimmy')
        room_1 = Room('The Heavy Room')
        room_1.check_in_guest(new_guest)
        self.assertEqual(True, (new_guest in room_1.room_guests))

    def test_check_out(self):
        new_guest = Guest('Jimmy')
        room_1 = Room('The Heavy Room')
        room_1.check_in_guest(new_guest)
        room_1.check_out_guest(new_guest)
        self.assertEqual(False, (new_guest in room_1.room_guests))

    def test_add_songs_to_rooms(self):
        room_1 = Room('The Heavy Room')
        room_1.add_song_to_room('Duality')
        self.assertEqual(True, 'Duality' in room_1.room_songs)


    