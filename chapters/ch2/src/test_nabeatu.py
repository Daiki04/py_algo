import pytest

if __name__ != "__main__":
    nabeatu_list = [i+1 if str(i+1).find("3") == -1 else "A" for i in range(100)]
    nabeatu_list[2::3] = ["A"] * len(nabeatu_list[2::3])

def get_nabeatu(num: int) -> str | int:
    return nabeatu_list[num-1]

@pytest.mark.parametrize("num, expected", [
    (1, 1),
    (2, 2),
    (3, "A"),
    (4, 4),
    (5, 5),
    (6, "A"),
    (7, 7),
    (8, 8),
    (9, "A"),
    (10, 10),
    (11, 11),
    (12, "A"),
    (13, "A"),
    (14, 14),
    (15, "A"),
    (16, 16),
    (17, 17),
    (18, "A"),
    (19, 19),
    (20, 20),
])

def test_get_nabeatu(num, expected):
    assert get_nabeatu(num) == expected

if __name__ == "__main__":
    num_input = int(input("Enter a number: "))
    nabeatu_list = [i+1 if str(i+1).find("3") == -1 else "A" for i in range(num_input)]
    nabeatu_list[2::3] = ["A"] * len(nabeatu_list[2::3])
    for i in range(1, num_input + 1):
        print(get_nabeatu(i))