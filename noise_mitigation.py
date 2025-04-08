"""
Implements basic noise mitigation techniques and explains their impact on optimization.
"""

from qiskit.providers.aer.noise import NoiseModel, depolarizing_error
from qiskit import Aer, execute, QuantumCircuit

def apply_noise_model():
    """
    Builds a simple depolarizing noise model for demonstration.
    """
    noise_model = NoiseModel()
    error = depolarizing_error(0.01, 1)
    noise_model.add_all_qubit_quantum_error(error, ['u1','u2','u3'])
    return noise_model

def run_with_noise(qc):
    """
    Executes the given circuit with a naive noise model and returns counts.
    """
    backend = Aer.get_backend('qasm_simulator')
    noise_model = apply_noise_model()
    job = execute(qc, backend, shots=1024, noise_model=noise_model)
    result = job.result()
    return result.get_counts()

def explain_noise_impact():
    """
    Symbolic explanation of how noise can alter measurement outcomes.
    """
    return ("Depolarizing noise randomly flips qubits, reducing fidelity. "
            "Mitigation often involves error correction or post-processing filters.")
