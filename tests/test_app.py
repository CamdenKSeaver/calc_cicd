import sys
from pathlib import Path
import pytest
import math
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add,sub,mult, div,log, square, sin, cos, sqrt,percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 5) == 5
def test_sub_negative():
    assert sub(-5, -3) == -2

def test_multiply():
    assert mult(5, 3) == 15



def test_multiply_negative():
    assert mult(-5, -3) == 15

def test_multiply_zero():
    assert mult(1, 0) == 0
def test_divide():
    assert div(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)

def test_log():
    assert log(1) == 0

def test_log_negative():
    with pytest.raises(ValueError):
        log(-1)

def test_log_zero():
    with pytest.raises(ValueError):
        log(0)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(10, 0)

def test_log_base_one():
    with pytest.raises(ValueError):
        log(10, 1)

def test_square():
    assert square(5) == 25



def test_sin():
    assert sin(math.pi / 2) == pytest.approx(1.0)

def test_cos():
    assert cos(math.pi) == pytest.approx(-1.0)

def test_sqrt():
    assert sqrt(4) == 2

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_percentage():
    assert percentage(50, 100) == 50.0

def test_percentage_zero_total():
        percentage(50, 0) == 0