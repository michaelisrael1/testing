import pytest
from logic.functions import mult_by_three, best_os

def test_best_os():
    assert best_os('linux') == True
    assert best_os('windows') is False
    assert best_os('mac') is False

def test_mult_by_three():
    assert mult_by_three(1) == 3
    assert mult_by_three(2) == 6
    assert mult_by_three(8) == 24