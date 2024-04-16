import pytest

# Function to get FizzBuzz
def get_fizzbuzz(num: int) -> str | int:
    fizz = "Fizz" if num % 3 == 0 else ""
    buzz = "Buzz" if num % 5 == 0 else ""
    fizzbuzz = fizz + buzz
    return fizzbuzz if fizzbuzz else num

# Test cases
@pytest.mark.parametrize("num, expected", [
    (1, 1),
    (2, 2),
    (3, "Fizz"),
    (4, 4),
    (5, "Buzz"),
    (6, "Fizz"),
    (7, 7),
    (8, 8),
    (9, "Fizz"),
    (10, "Buzz"),
    (11, 11),
    (12, "Fizz"),
    (13, 13),
    (14, 14),
    (15, "FizzBuzz"),
    (16, 16),
    (17, 17),
    (18, "Fizz"),
    (19, 19),
    (20, "Buzz"),
])

def test_get_fizzbuzz(num, expected):
    assert get_fizzbuzz(num) == expected

if __name__ == "__main__":
    num_input = int(input("Enter a number: "))
    for i in range(1, num_input + 1):
        print(get_fizzbuzz(i))