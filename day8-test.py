from day8 import *


def test_empty_string():
    assert character_count('""') == 0


def test_characters_only():
    assert character_count('"abc"') == 3
