from src.problems.algorithms.warmup.diagonal_difference.main import DiagonalDifference

def test_3x3_matrix():
    matrix = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    dd = DiagonalDifference(matrix)
    assert dd.calculate() == 15

def test_2x2_matrix():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    dd = DiagonalDifference(matrix)
    assert dd.calculate() == 0

