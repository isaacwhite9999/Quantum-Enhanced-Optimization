"""
Creates a parameterized quantum circuit (ansatz) for general optimization problems.
"""

import numpy as np
from qiskit import QuantumCircuit

def build_parametric_ansatz(num_qubits, reps=2):
    """
    Constructs a parameterized ansatz with layered rotations and entangling gates.
    Returns a QuantumCircuit with the required parameters in place.
    """
    qc = QuantumCircuit(num_qubits)
    # Example: Reps layers of RX, RZ, then CNOT entangling
    # We'll store parameters as {theta_i} for each gate
    for rep in range(reps):
        for qb in range(num_qubits):
            qc.rx(0.1, qb)  # placeholder; in practice, use Parameter objects
            qc.rz(0.2, qb)
        for qb in range(num_qubits-1):
            qc.cx(qb, qb+1)
    return qc
