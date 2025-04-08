import pytest
from qiskit import QuantumCircuit
from noise_mitigation import run_with_noise

def test_run_with_noise():
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)
    counts = run_with_noise(qc)
    assert isinstance(counts, dict)
