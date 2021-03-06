from day8 import *


def test_empty_string():
    assert character_count(r'""') == 0


def test_characters_only():
    assert character_count(r'"abc"') == 3


def test_single_escaped_character():
    assert character_count(r'"aaa\"aaa"') == 7


def test_hexadecimal_character():
    assert character_count(r'"\x27"') == 1


def test_escaped_slash_before_x():
    assert character_count(r'"\\x27"') == 4


def test_double_slash():
    assert character_count(r'"\\"') == 1
