import pytest
from qiskit import QuantumCircuit
from quantum_circuit_debugger import debug_quantum_circuit, explain_debugging_issue

def test_debug_quantum_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0,1)
    result = debug_quantum_circuit(qc)
    assert result == "No gate errors detected."
