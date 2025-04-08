import pytest
from parametric_ansatz import build_parametric_ansatz

def test_build_parametric_ansatz():
    qc = build_parametric_ansatz(num_qubits=3, reps=2)
    assert qc.num_qubits == 3
    # Just ensure we have some gates
    assert qc.data, "Circuit should not be empty."
