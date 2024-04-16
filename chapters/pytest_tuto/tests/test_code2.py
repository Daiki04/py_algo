import pytest
import os

dir = os.path.dirname(__file__)

from src import code2

# 下記はすべて同じテストを行っている

### 通常のテスト
# def test_diff_numbers():
#     assert code2.diff_numbers(1, 2) == -1
#     assert code2.diff_numbers(2, 1) == 1
#     assert code2.diff_numbers(0, 0) == 0
#     assert code2.diff_numbers(-1, -2) == 1
#     assert code2.diff_numbers(-2, -1) == -1

## パラメータ化テスト
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (2, 1, 1),
    (0, 0, 0),
    (-1, -2, 1),
    (-2, -1, -1),
])

def test_diff_numbers(a, b, expected):
    assert code2.diff_numbers(a, b) == expected

### テキストファイルから入力を受け取ってテスト
# def test_diff_numbers_from_file():
#     with open(os.path.join(dir, "numbers.txt")) as f:
#         for line in f:
#             a, b, expected = map(int, line.split(" "))
#             assert code2.diff_numbers(a, b) == expected