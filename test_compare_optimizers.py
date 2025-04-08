import pytest
from compare_optimizers import compare_optimizers

def dummy_objective(x):
    return sum(val*val for val in x)  # simple parabola

def test_compare_optimizers():
    init_point = [0.5, -0.5]
    results = compare_optimizers(dummy_objective, init_point, maxiter=5)
    assert 'COBYLA' in results
    assert 'SPSA' in results
    assert 'ADAM' in results
