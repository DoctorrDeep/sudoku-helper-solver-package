import pytest

from ambars_sudoku_solver.sudoku_cube import Sudoku

test_data: list[tuple[range | list[int], bool]] = [
    (range(1, 10), True),
    (range(2, 11), False),
    (range(9), True),
    ([0, 1, 2, 0, 4, 0, 6, 7, 8], True),
    ([1, 9, 2, 1, 4, 1, 6, 7, 1], False),
]


@pytest.mark.parametrize("check_input,expected", test_data)
def test_do_check(check_input, expected):
    assert Sudoku.check(check_input) == expected


@pytest.mark.parametrize("check_input,expected", test_data)
def test_do_strict_check(check_input, expected):
    modified_expected = expected if 0 not in check_input else False
    assert Sudoku.strict_check(check_input) == modified_expected
