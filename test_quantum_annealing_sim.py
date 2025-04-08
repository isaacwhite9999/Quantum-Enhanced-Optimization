import pytest
from quantum_annealing_sim import simulated_quantum_annealing, explain_annealing_results

def test_simulated_quantum_annealing():
    final_state = simulated_quantum_annealing(num_steps=5)
    assert 0 <= abs(final_state) < 2.0  # just a broad check
