from ambars_sudoku_solver.helpers.generate_problems import create_sudoku_problem
from ambars_sudoku_solver.helpers.types import Level

EASY_SUDOKU = create_sudoku_problem(level=Level.easy)
DIFFICULT_SUDOKU = create_sudoku_problem(level=Level.difficult)


def test_make_easy_problem():
    assert EASY_SUDOKU.get_max_suggestions_count() in [2, 3]


def test_make_difficult_problem():
    assert DIFFICULT_SUDOKU.get_max_suggestions_count() in [3, 4]
