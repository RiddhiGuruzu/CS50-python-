import pytest
from seasons import DateOfBirth

def test_invalid_date_format():
    with pytest.raises(SystemExit):
        DateOfBirth("February 6th, 1998")
    with pytest.raises(SystemExit):
        DateOfBirth("1998/02/06")
    with pytest.raises(SystemExit):
        DateOfBirth("06-02-1998")

def test_invalid_calendar_date():
    with pytest.raises(SystemExit):
        DateOfBirth("2021-02-31")
    with pytest.raises(SystemExit):
        DateOfBirth("2021-13-01")


def test_valid_date_creation():
    dob = DateOfBirth("2000-01-01")
    assert dob is not None