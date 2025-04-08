import pytest
from qiskit import QuantumCircuit
from uncertainty_quantification import run_uncertainty_quantification

def test_run_uncertainty_quantification():
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)
    entropy = run_uncertainty_quantification(qc)
    assert entropy >= 0
