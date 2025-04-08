"""
A quantum circuit debugger that checks for gate errors or invalid qubit indices
and provides symbolic explanations if found.
"""

import ast

def debug_quantum_circuit(qc):
    """
    In a real scenario, we'd parse the Qiskit instructions.
    For demonstration, let's do a naive check that each gate index is in range.
    """
    num_qubits = qc.num_qubits
    for instr, qargs, cargs in qc.data:
        for qa in qargs:
            if qa.index >= num_qubits:
                return f"Gate {instr.name} uses out-of-range qubit index {qa.index}"
    return "No gate errors detected."

def explain_debugging_issue(issue_str):
    """
    Symbolic explanation of the debug result.
    """
    if "out-of-range qubit index" in issue_str:
        return "A gate references a qubit that doesn't exist in the circuit."
    return "No issues."
