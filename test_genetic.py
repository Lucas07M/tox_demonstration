import pytest
from genetic import *


def test_fitness_nq():
    x = [5, 7, 1, 2, 0, 3, 4, 6]
    assert fitness_nq(x) == 12


def test_get_best_solution():
    x = [[5, 7, 1, 2, 0, 3, 4, 6],
         [0, 1, 2, 3, 4, 5, 6, 7],
         [7, 5, 2, 4, 1, 0, 3, 6]]
    y = [fitness_nq(item) for item in x]
    assert get_best_solution(y) == 2
