from main import calculate, BadInput
import pytest
@pytest.mark.parametrize("d1, op, d2, ans, degrees, expected, roundTo", [
    ("2", "+", "3", None, False, 5, 5),
    ("5", "-", "2", None, False, 3, 5),
    ("4", "*", "2", None, False, 8, 5),
    ("8", "/", "2", None, False, 4, 5),
    ("9", "^", "2", None, False, 81, 5),
    ('27','/^','3', None, False, 3, 5),
    ('32', 'log', '2', None, False, 5, 5),
    ('ans','%', '2', 10, False, 0, 5),
    ("16", "sqrt", None, None, False, 4, 5),
    ("pi", "sin", None, None, False, 0, 5),
    ("tau", "cos", None, None, False, 1, 5),
    ("180", "tan", None, None, True, 0, 5),
    ("2", "ln", None, None, False, 0.69315, 5),
    ("5", "!", None, None, False, 120, 5),
    ("2", "atan", None, None, True, 63.43495, 5),
    ("1", "asin", None, None, True, 90, 5),
    ("0.5", "acos", None, None, True, 60, 5)
])
def test_operations(d1, op, d2, ans, degrees, expected, roundTo):
    result = calculate(d1, op, d2, ans, degrees, roundTo)
    assert result == expected
def test_bad_input():
    with pytest.raises(BadInput):
        calculate('ans', '/', '2', None, False, 5)