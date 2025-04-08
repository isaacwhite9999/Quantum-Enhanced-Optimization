import argparse
import sys
from basic_qiskit_circuit import build_basic_circuit, run_circuit_simulation

def main():
    parser = argparse.ArgumentParser(description="Basic Qiskit Circuit Simulator")
    parser.add_argument("--num-qubits", type=int, default=2,
                        help="Number of qubits to use in the circuit (default: 2)")
    args = parser.parse_args()

    try:
        qc = build_basic_circuit(num_qubits=args.num_qubits)
        print("=== Quantum Circuit ===")
        print(qc.draw(output='text'))

        counts = run_circuit_simulation(qc)
        print("\n=== Simulation Results (Measurement Counts) ===")
        print(counts)
    except Exception as e:
        sys.exit(f"Error running quantum circuit: {str(e)}")

if __name__ == "__main__":
    main()
