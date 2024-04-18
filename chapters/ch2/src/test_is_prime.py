import pytest

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Test cases
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
    (12, False),
    (13, True),
    (14, False),
    (15, False),
    (16, False),
    (17, True),
    (18, False),
    (19, True),
    (20, False),
])

def test_is_prime(num, expected):
    assert is_prime(num) == expected