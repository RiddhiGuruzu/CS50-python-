from working import convert
import pytest

def test_am_to_pm():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_pm_to_am():
    assert convert("10:30 PM to 8:00 AM") == "22:30 to 08:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("10:00 PM to 8 AM") == "22:00 to 08:00"


def test_value_errors():
    # Invalid hour/minute values
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    # Invalid formats / wrong separators
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
