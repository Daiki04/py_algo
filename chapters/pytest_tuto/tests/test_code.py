from src import code

def test_sum_numbers():
    result1, result2 = code.sum_numbers(1, 2)
    assert result1 == 3
    assert result2 == 1
    # assert result == 4  # This will fail