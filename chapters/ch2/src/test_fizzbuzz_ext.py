import pytest

if __name__ != "__main__":
    fizzbuzz_list = [i+1 for i in range(100)]
    fizzbuzz_list[2::3] = ["Fizz"] * len(fizzbuzz_list[2::3])
    fizzbuzz_list[4::5] = ["Buzz"] * len(fizzbuzz_list[4::5])
    fizzbuzz_list[14::15] = ["FizzBuzz"] * len(fizzbuzz_list[14::15])

# Function to get FizzBuzz
def get_fizzbuzz(num: int) -> str | int:
    return fizzbuzz_list[num-1]

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
    fizzbuzz_list = [i+1 for i in range(num_input)]
    fizzbuzz_list[2::3] = ["Fizz"] * len(fizzbuzz_list[2::3])
    fizzbuzz_list[4::5] = ["Buzz"] * len(fizzbuzz_list[4::5])
    fizzbuzz_list[14::15] = ["FizzBuzz"] * len(fizzbuzz_list[14::15])
    for i in range(1, num_input + 1):
        print(get_fizzbuzz(i))