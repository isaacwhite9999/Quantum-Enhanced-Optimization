"""
Implements a basic Variational Quantum Eigensolver (VQE) for a simple Hamiltonian.
Uses Qiskit's VQE libraries, or builds a custom routine.
"""

import numpy as np
from qiskit import Aer, execute
from qiskit.circuit.library import RealAmplitudes
from qiskit.opflow import PauliSumOp, Z
from qiskit.algorithms import VQE
from qiskit.algorithms.optimizers import COBYLA

def run_vqe_eigensolver():
    """
    Demonstrates a minimal VQE setup for the Hamiltonian H = Z (single-qubit).
    Returns the computed ground state energy.
    """
    # Define a simple 1-qubit Z Hamiltonian
    hamiltonian = PauliSumOp.from_list([("Z", 1.0)])

    # Use a basic ansatz
    ansatz = RealAmplitudes(num_qubits=1, reps=1)

    # Initialize VQE
    optimizer = COBYLA(maxiter=100)
    vqe = VQE(ansatz, optimizer=optimizer, quantum_instance=Aer.get_backend('statevector_simulator'))

    # Compute ground state
    result = vqe.compute_minimum_eigenvalue(operator=hamiltonian)
    return result.eigenvalue.real
