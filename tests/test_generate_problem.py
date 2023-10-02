from ambars_sudoku_solver.helpers.generate_problems import create_sudoku_problem
from ambars_sudoku_solver.helpers.types import Level
from ambars_sudoku_solver.sudoku_cube import Sudoku

EASY_SUDOKU: Sudoku = create_sudoku_problem(level=Level.EASY)
DIFFICULT_SUDOKU: Sudoku = create_sudoku_problem(level=Level.DIFFICULT)


def test_make_easy_problem() -> None:
    assert EASY_SUDOKU.get_max_suggestions_count() in [2, 3]


def test_make_difficult_problem() -> None:
    assert DIFFICULT_SUDOKU.get_max_suggestions_count() in [3, 4]
