import pytest
from arithmetic import subtract, add, find_duplicates_in_set

def test_add():
    result = add(10,12)
    assert result == 22

def test_subtract():
    result = subtract(10,2)
    assert result == 8

def test_find_duplicates_in_set():
    result = find_duplicates_in_set([11,22,33,22,55])
    assert result == [22]


