import pytest
import json
import datetime
from tennis_scoring.scoring import is_even,paul

def test_is_even():
    assert is_even(2) == True

def test_paul():
    assert paul(['life', 'eating', 'life']) == 'Super happy!'
    assert paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']) == 'Super happy!'
    assert paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']) == 'Happy!'

