import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

# 1. Create guests

    def test_create_guest(self):
        new_guest = Guest('Max')
        self.assertEqual('Max', new_guest.guest_name)

