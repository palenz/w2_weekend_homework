import unittest
from src.song import Song

class TestSong(unittest.TestCase):

# 1. Create songs

    def test_create_song(self):
        new_song = Song('Duality')
        self.assertEqual('Duality', new_song.song_name)