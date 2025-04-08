"""
Implements uncertainty quantification for quantum circuit outcomes using a symbolic approach.
"""

import numpy as np
from qiskit import Aer, execute

def measure_distribution(qc, shots=1024):
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

def quantify_uncertainty(counts):
    """
    E.g., compute Shannon entropy as a measure of outcome uncertainty.
    """
    total = sum(counts.values())
    entropy = 0.0
    for c in counts.values():
        p = c/total
        if p > 0:
            entropy -= p * np.log2(p)
    return entropy

def run_uncertainty_quantification(qc):
    counts = measure_distribution(qc)
    return quantify_uncertainty(counts)
