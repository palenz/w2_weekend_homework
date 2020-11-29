import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

# 1. Create rooms

    def test_create_room(self):
        new_room = Room('The Heavy Room')
        self.assertEqual('The Heavy Room', new_room.room_name)

    def test_check_in(self):
        new_guest = Guest('Jimmy', 20)
        room_1 = Room('The Heavy Room')
        room_1.check_in_guest(new_guest)
        self.assertEqual(True, (new_guest in room_1.room_guests))

    def test_check_out(self):
        new_guest = Guest('Jimmy', 20)
        room_1 = Room('The Heavy Room')
        room_1.check_in_guest(new_guest)
        room_1.check_out_guest(new_guest)
        self.assertEqual(False, (new_guest in room_1.room_guests))

    def test_add_songs_to_rooms(self):
        room_1 = Room('The Heavy Room')
        room_1.add_song_to_room('Duality')
        self.assertEqual(True, 'Duality' in room_1.room_songs)

    def test_room_capacity(self):
        new_guest = Guest('Jimmy', 20)
        room_1 = Room('The Heavy Room')
        guest = [new_guest]
        max_guests = guest*51
        for guest in max_guests: 
            room_1.check_in_guest(guest) 
        self.assertEqual(50, len(room_1.room_guests))

    def test_deny_entry_ur_broke(self):
        broke_lad = Guest('Elliot', 1)
        room_1 = Room('80s')
        room_1.check_in_guest(broke_lad)
        self.assertEqual(0, len(room_1.room_guests))