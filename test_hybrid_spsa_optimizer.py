import pytest
from hybrid_spsa_optimizer import run_spsa_optimization

def dummy_qc_builder(params):
    from qiskit import QuantumCircuit
    qc = QuantumCircuit(1)
    return qc

def test_run_spsa_optimization():
    result = run_spsa_optimization(dummy_qc_builder, maxiter=5)
    assert len(result) == 2
