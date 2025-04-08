"""
Visualizes the quantum state evolution over iterations.
Could store intermediate states and plot them with Bloch spheres or other means.
"""

import matplotlib.pyplot as plt
from qiskit import Aer, execute
from qiskit.quantum_info import Statevector

def visualize_state_evolution(qc_list):
    """
    Takes a list of circuits (one per iteration),
    extracts the quantum state, and plots some representation.
    For a minimal approach, just print Bloch sphere data for the first qubit.
    """
    states_data = []
    for qc in qc_list:
        backend = Aer.get_backend('statevector_simulator')
        job = execute(qc, backend)
        result = job.result()
        state = result.get_statevector(qc)
        sv = Statevector(state)
        states_data.append(sv)

    # Basic approach: just print out first circuit's state
    if states_data:
        print("Example statevector of last circuit:", states_data[-1].data)
    # If you want actual Bloch sphere, you'd do advanced plotting here.

def demo_visualization():
    """
    Simple demonstration that calls visualize_state_evolution with two circuits.
    """
    from qiskit import QuantumCircuit
    qc1 = QuantumCircuit(1)
    qc1.h(0)
    qc2 = QuantumCircuit(1)
    qc2.x(0)

    visualize_state_evolution([qc1, qc2])
