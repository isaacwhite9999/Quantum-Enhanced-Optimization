import pytest
from adaptive_variational_tuning import run_adaptive_variational_tuning

def test_run_adaptive_variational_tuning():
    qc = run_adaptive_variational_tuning(steps=4)
    assert qc.num_qubits == 1
    assert len(qc.data) > 0
