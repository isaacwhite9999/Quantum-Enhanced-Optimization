import pytest
from qiskit import QuantumCircuit
from circuit_depth_optimizer import reduce_circuit_depth, analyze_depth_reduction

def test_reduce_circuit_depth():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.h(0)
    qc.cx(0,1)
    optimized = reduce_circuit_depth(qc)
    msg = analyze_depth_reduction(qc, optimized)
    assert isinstance(msg, str)

