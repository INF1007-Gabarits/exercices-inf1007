#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from unittest import mock
from music_library import Song, Playlist


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Blinding Lights", "The Weeknd", 200, "Pop")
        self.song2 = Song("Shape of You", "Ed Sheeran", 240, "Pop")

    def test_init(self):
        self.assertEqual(self.song1.title, "Blinding Lights")
        self.assertEqual(self.song1.artist, "The Weeknd")
        self.assertEqual(self.song1.duration, 200)
        self.assertEqual(self.song1.genre, "Pop")

    def test_to_dict(self):
        expected_dict = {
            "title": "Blinding Lights",
            "artist": "The Weeknd",
            "duration": 200,
            "genre": "Pop",
        }
        self.assertEqual(self.song1.to_dict(), expected_dict)

    def test_str(self):
        self.assertEqual(
            str(self.song1),
            "Blinding Lights by The Weeknd - 3:20 (Pop)"
        )


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Blinding Lights", "The Weeknd", 200, "Pop")
        self.song2 = Song("Shape of You", "Ed Sheeran", 240, "Pop")
        self.song3 = Song("Bohemian Rhapsody", "Queen", 360, "Rock")
        self.playlist = Playlist("My Favorites")
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song3)

    def test_add_song(self):
        self.assertEqual(len(self.playlist.songs), 3)
        new_song = Song("Hotel California", "Eagles", 390, "Rock")
        self.playlist.add_song(new_song)
        self.assertEqual(len(self.playlist.songs), 4)

    def test_sort_songs(self):
        self.playlist.sort_songs("title")
        self.assertEqual(self.playlist.songs[0].title, "Blinding Lights")
        self.assertEqual(self.playlist.songs[1].title, "Bohemian Rhapsody")
        self.assertEqual(self.playlist.songs[2].title, "Shape of You")

    def test_total_duration(self):
        self.assertEqual(self.playlist.total_duration(), 800)

    def test_display(self):
        with mock.patch("builtins.print") as mocked_print:
            self.playlist.display()
            mocked_print.assert_any_call("Playlist: My Favorites")
            mocked_print.assert_any_call(
                "1. Blinding Lights by The Weeknd - 3:20 (Pop)"
            )
            mocked_print.assert_any_call(
                "2. Shape of You by Ed Sheeran - 4:00 (Pop)"
            )
            mocked_print.assert_any_call(
                "3. Bohemian Rhapsody by Queen - 6:00 (Rock)"
            )

    def test_export_to_json(self):
        with mock.patch("builtins.open", mock.mock_open()) as mocked_file:
            self.playlist.export_to_json("test.json")
            mocked_file.assert_called_with("test.json", "w", encoding="utf-8")


if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.mkdir("logs")
    with open("logs/tests_results.txt", "w") as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
    print(open("logs/tests_results.txt", "r").read())
