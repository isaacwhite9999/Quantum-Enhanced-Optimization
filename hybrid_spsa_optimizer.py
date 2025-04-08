"""
Implements a hybrid quantum-classical optimizer using the SPSA (Simultaneous Perturbation Stochastic Approximation) algorithm.
"""

import numpy as np
from qiskit import Aer, execute
from qiskit.algorithms.optimizers import SPSA

def sample_objective(params, qc_builder, backend=None):
    """
    Evaluate the cost of a quantum circuit built with 'params' on a given backend.
    For demonstration, returns random cost.
    """
    qc = qc_builder(params)
    if backend is None:
        backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    # Example cost: random
    return np.random.rand()

def run_spsa_optimization(qc_builder, maxiter=50):
    """
    Minimizes sample_objective via SPSA.
    """
    optimizer = SPSA(maxiter=maxiter)
    initial_point = [0.1, 0.1]  # placeholder

    def spsa_fn(params):
        return sample_objective(params, qc_builder)

    result, _, _ = optimizer.optimize(num_vars=len(initial_point), objective_function=spsa_fn, initial_point=initial_point)
    return result
