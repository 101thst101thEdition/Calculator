from main import calculate, BadInput
import pytest
@pytest.mark.parametrize("d1, op, d2, ans, degrees, expected", [
    ("2", "+", "3", None, False, 5),
    ("5", "-", "2", None, False, 3),
    ("4", "*", "2", None, False, 8),
    ("8", "/", "2", None, False, 4),
    ("9", "^", "2", None, False, 81),
    ('27','/^','3', None, False, 3),
    ('32', 'log', '2', None, False, 5),
    ('ans','%', '2', 10, False, 0),
    ("16", "sqrt", None, None, False, 4),
    ("pi", "sin", None, None, False, 0),
    ("tau", "cos", None, None, False, 1),
    ("180", "tan", None, None, True, 0),
    ("2", "ln", None, None, False, 0.69315),
    ("5", "!", None, None, False, 120),
    ("2", "atan", None, None, True, 63.43495),
    ("1", "asin", None, None, True, 90),
    ("0.5", "acos", None, None, True, 60)
])
def test_operations(d1, op, d2, ans, degrees, expected):
    result = calculate(d1, op, d2, ans, degrees)
    assert result == expected
def test_bad_input():
    with pytest.raises(BadInput):
        calculate('ans', '/', '2', None, False)