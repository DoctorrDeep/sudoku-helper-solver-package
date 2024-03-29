import copy
import random

from ambars_sudoku_solver.helpers import ALL_XYS
from ambars_sudoku_solver.helpers.errors import SolverTimeoutError, UnknownSolutionError
from ambars_sudoku_solver.helpers.timer import timer
from ambars_sudoku_solver.helpers.types import Level, SudokuCellLocations, SudokuSquare
from ambars_sudoku_solver.settings import (
    COUNT_OF_CELLS_TO_FILL,
    MAX_SUGGESTIONS_DIFFICULT,
    MAX_SUGGESTIONS_EASY,
    TIMEOUT_FOR_RECURSION,
)
from ambars_sudoku_solver.solvers.backtracking_solution import solve_square
from ambars_sudoku_solver.sudoku_cube import Sudoku

MAX_COUNT_OF_CELLS_TO_EMPTY: int = 30
MAX_SUGGESTION_SETTINGS: dict[Level, int] = {
    Level.EASY: MAX_SUGGESTIONS_EASY,
    Level.DIFFICULT: MAX_SUGGESTIONS_DIFFICULT,
}


@timer
def create_sudoku_problem(level: Level) -> Sudoku:
    """
    Generate a solved sudoku cube and start removing
    numbers till the highest number of solutions
    to any cell in the full square exceeds 2
    """

    def generate_empty_square_with_random_fills() -> Sudoku:
        """
        Generate an empty sudoku square and fill a few spots in randomly but without breaking rules
        """
        empty_square: SudokuSquare = [[0] * 9 for _ in range(9)]
        spots_filled: int = 0
        while spots_filled <= COUNT_OF_CELLS_TO_FILL:
            rand_xy = random.choice(ALL_XYS)
            empty_square[rand_xy[0]][rand_xy[1]] = random.choice(range(1, 10))
            if Sudoku.check_solution(empty_square):
                spots_filled += 1
            else:
                empty_square[rand_xy[0]][rand_xy[1]] = 0

        sudoku = Sudoku(empty_square)
        return sudoku

    def generate_sudoku_square() -> Sudoku:
        """
        Use backtracking to fill in a partially filled square.
        """

        try:
            sudoku: Sudoku = generate_empty_square_with_random_fills()
            sudoku.run_solver(solve_square)
        except SolverTimeoutError:
            # If timeout reached, try one more time with a new square.
            sudoku = generate_empty_square_with_random_fills()
            sudoku.run_solver(solve_square, timeout=TIMEOUT_FOR_RECURSION + 5)
        return sudoku

    sudoku_square: Sudoku = generate_sudoku_square()
    if sudoku_square.solutions:
        sudoku_square.sudoku_square = random.choice(sudoku_square.solutions)
    else:
        raise UnknownSolutionError("Generated problem with empty solutions.")
    sudoku_square.sudoku_square_copy = copy.deepcopy(sudoku_square.sudoku_square)
    elements_to_empty: SudokuCellLocations = random.sample(ALL_XYS, MAX_COUNT_OF_CELLS_TO_EMPTY)
    for loc in elements_to_empty:
        sudoku_square.sudoku_square[loc[0]][loc[1]] = 0
        sudoku_square.sudoku_square_copy[loc[0]][loc[1]] = 0
        sudoku_square.update_suggestions()
        if sudoku_square.get_max_suggestions_count() >= MAX_SUGGESTION_SETTINGS.get(level, 0):
            return sudoku_square

    raise UnknownSolutionError(
        f"Number of suggestions remains low even after removing {MAX_COUNT_OF_CELLS_TO_EMPTY} out of 81 cells"
    )
