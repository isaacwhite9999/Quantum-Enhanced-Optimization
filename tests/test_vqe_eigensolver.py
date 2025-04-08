import pytest
from vqe_eigensolver import run_vqe_eigensolver

def test_run_vqe_eigensolver():
    energy = run_vqe_eigensolver()
    # For H = Z, the ground state energy should be -1.0 ideally
    assert energy < 0, "Expected negative ground state energy for Z operator."
