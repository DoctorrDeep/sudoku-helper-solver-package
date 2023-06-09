import os

MAX_COUNT_OF_CELLS_TO_EMPTY = float(os.getenv("MAX_COUNT_OF_CELLS_TO_EMPTY", 30))
MAX_SUGGESTIONS_EASY = float(os.getenv("MAX_SUGGESTIONS_EASY", 2))
MAX_SUGGESTIONS_DIFFICULT = float(os.getenv("MAX_SUGGESTIONS_DIFFICULT", 3))
COUNT_OF_CELLS_TO_FILL = float(os.getenv("COUNT_OF_CELLS_TO_FILL", 9))
TIMEOUT_FOR_RECURSION = float(os.getenv("TIMEOUT_FOR_RECURSION", 2))
MAX_SOLUTIONS = float(os.getenv("MAX_SOLUTIONS", 5))
