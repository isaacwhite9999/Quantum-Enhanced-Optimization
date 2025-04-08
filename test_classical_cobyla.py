import pytest
from classical_cobyla import run_cobyla_optimization

def dummy_builder(params):
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(1)
    # Just a placeholder
    return qc

def test_run_cobyla_optimization():
    result = run_cobyla_optimization(dummy_builder, maxiter=5)
    assert len(result) == 2, "Expecting a param vector of length 2."
