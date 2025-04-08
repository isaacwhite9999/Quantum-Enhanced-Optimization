"""
Builds a tool to compare different classical optimizers (COBYLA, SPSA, etc.) on a quantum objective.
"""

from qiskit.algorithms.optimizers import COBYLA, SPSA, ADAM
import numpy as np

def compare_optimizers(objective_fn, initial_point, maxiter=50):
    """
    objective_fn(params) => cost
    Returns a dictionary of { 'COBYLA': best_params, 'SPSA': best_params, ... } 
    for each optimizer, along with final cost.
    """
    results = {}

    opt_cobyla = COBYLA(maxiter=maxiter)
    def cobyla_fn(x):
        return objective_fn(x)
    cobyla_result, cost, _ = opt_cobyla.optimize(len(initial_point), cobyla_fn, initial_point=initial_point)
    results['COBYLA'] = (cobyla_result, cost)

    opt_spsa = SPSA(maxiter=maxiter)
    def spsa_fn(x):
        return objective_fn(x)
    spsa_result, cost_spsa, _ = opt_spsa.optimize(len(initial_point), spsa_fn, initial_point=initial_point)
    results['SPSA'] = (spsa_result, cost_spsa)

    # ADAM for demonstration
    opt_adam = ADAM(maxiter=maxiter)
    def adam_fn(x):
        return objective_fn(x)
    adam_result, cost_adam, _ = opt_adam.optimize(len(initial_point), adam_fn, initial_point=initial_point)
    results['ADAM'] = (adam_result, cost_adam)

    return results
