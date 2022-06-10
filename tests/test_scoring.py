import pytest
import json
import datetime
from tennis_scoring.scoring import is_even

def test_is_even():
    assert is_even(2) == True

