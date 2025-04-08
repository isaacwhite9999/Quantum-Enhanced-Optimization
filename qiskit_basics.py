"""
A simple Python module demonstrating a basic quantum circuit with Qiskit.

- Builds a minimal circuit (Hadamard on qubit 0, then CNOT to qubit 1).
- Measures all qubits.
- Runs the circuit on the local 'qasm_simulator'.
"""

from qiskit import QuantumCircuit, Aer, execute

def build_basic_circuit(num_qubits=2):
    """
    Constructs a minimal quantum circuit with the specified number of qubits.
    Applies a Hadamard on qubit 0, then a CNOT from qubit 0->1 (if at least 2 qubits),
    and measures all qubits.
    """
    qc = QuantumCircuit(num_qubits, num_qubits)
    qc.h(0)
    if num_qubits > 1:
        qc.cx(0, 1)
    qc.measure(range(num_qubits), range(num_qubits))
    return qc

def run_circuit_simulation(qc):
    """
    Executes the given quantum circuit on the local 'qasm_simulator'
    and returns the dictionary of measurement outcomes.
    """
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    return counts
