from day8 import *


def test_empty_string():
    assert character_count(r'""') == 0


def test_characters_only():
    assert character_count(r'"abc"') == 3


def test_single_escaped_character():
    assert character_count(r'"aaa\"aaa"') == 7
