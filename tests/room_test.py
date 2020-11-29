import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

# 1. Create rooms

    def test_create_room(self):
        new_room = Room('The Heavy Room', 'Duality')
        self.assertEqual('The Heavy Room', new_room.room_name)

    def test_check_in(self):
        new_guest = Guest('Jimmy')
        room_1 = Room('The Heavy Room', 'Duality')
        room_1.check_in_guest(new_guest)
        self.assertEqual(True, (new_guest in room_1.room_guests))

    def test_check_out(self):
        new_guest = Guest('Jimmy')
        room_1 = Room('The Heavy Room', 'Duality')
        room_1.check_in_guest(new_guest)
        room_1.check_out_guest(new_guest)
        self.assertEqual(False, (new_guest in room_1.room_guests))


    