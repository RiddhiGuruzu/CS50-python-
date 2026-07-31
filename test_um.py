import pytest
from um import count

def test_single_um():
    assert count("um?") == 1
    assert count("Um, thanks for the help.") == 1

def test_multiple_ums():
    assert count("Um, thanks, um, for the album.") == 2
    assert count("um, um, um!") == 3

def test_substring_matches():
    assert count("yummy") == 0
    assert count("album") == 0
