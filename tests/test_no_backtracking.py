import pytest

from ambars_sudoku_solver.helpers.errors import UnknownSolutionError
from ambars_sudoku_solver.helpers.types import SudokuCellLocation
from ambars_sudoku_solver.solvers.no_backtracking_solution import try_fill_in
from ambars_sudoku_solver.sudoku_cube import Sudoku
from tests.data import EASY_SUDOKU, SOLVED_SUDOKU, UNSOLVABLE_SUDOKU

SUDOKU: Sudoku = Sudoku(EASY_SUDOKU)
SUDOKU.run_solver(try_fill_in)

test_solution_and_length_of_suggestions = [
    (SUDOKU.solutions[0], SOLVED_SUDOKU),
    (len(SUDOKU.solutions), 1),
    (len(SUDOKU.suggestions.keys()), 3),
]

test_suggestions: list[tuple[SudokuCellLocation, list[int]]] = [
    ((2, 2), [4]),
    ((5, 6), [2]),
    ((6, 1), [9]),
]


@pytest.mark.parametrize("test_data,expected", test_solution_and_length_of_suggestions)
def test_easy_no_backtracking_solution(test_data, expected):
    assert test_data == expected


@pytest.mark.parametrize("test_data,expected", test_suggestions)
def test_easy_no_backtracking_suggestions(test_data, expected):
    assert SUDOKU.suggestions[test_data] == expected


def test_unsolvable_problem():
    sudoku = Sudoku(UNSOLVABLE_SUDOKU)
    with pytest.raises(UnknownSolutionError):
        sudoku.run_solver(try_fill_in)
