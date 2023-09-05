import pytest
from utilities import *

def test_add_time():
    assert add_time("00:00", "23:59") == 1439
    # assert add_time("00:00", "23:59") == 1438
