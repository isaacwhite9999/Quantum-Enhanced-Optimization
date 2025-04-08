import sys
import argparse
from basic_qiskit_circuit import build_basic_circuit, run_circuit_simulation

# New modules
from vqe_eigensolver import run_vqe_eigensolver
from parametric_ansatz import build_parametric_ansatz
from classical_cobyla import run_cobyla_optimization
from hybrid_spsa_optimizer import run_spsa_optimization
from quantum_state_visualizer import demo_visualization
from quantum_circuit_debugger import debug_quantum_circuit, explain_debugging_issue
from noise_mitigation import run_with_noise, explain_noise_impact
from compare_optimizers import compare_optimizers
from quantum_annealing_sim import simulated_quantum_annealing, explain_annealing_results
from circuit_depth_optimizer import reduce_circuit_depth, analyze_depth_reduction

def main():
    parser = argparse.ArgumentParser(description="Quantum Optimization CLI")
    
    # Existing example from your basic circuit
    parser.add_argument("--basic-circuit", action="store_true", help="Build & run a simple circuit.")
    parser.add_argument("--num-qubits", type=int, default=2, help="Number of qubits for basic circuit.")

    # The next 10 features
    parser.add_argument("--vqe", action="store_true", help="Run VQE on a simple Hamiltonian.")
    parser.add_argument("--parametric-ansatz", action="store_true", help="Show parametric ansatz.")
    parser.add_argument("--cobyla-opt", action="store_true", help="Test classical COBYLA optimization.")
    parser.add_argument("--spsa-opt", action="store_true", help="Test SPSA hybrid optimization.")
    parser.add_argument("--visualize-states", action="store_true", help="Visualize quantum state evolution.")
    parser.add_argument("--circuit-debug", action="store_true", help="Debug a quantum circuit for gate errors.")
    parser.add_argument("--noise-test", action="store_true", help="Run circuit with noise model.")
    parser.add_argument("--compare-opts", action="store_true", help="Compare multiple classical optimizers.")
    parser.add_argument("--anneal-sim", action="store_true", help="Simulate quantum annealing.")
    parser.add_argument("--depth-opt", action="store_true", help="Optimize circuit depth and analyze result.")

    args = parser.parse_args()

    # If user wants the basic circuit
    if args.basic_circuit:
        qc = build_basic_circuit(num_qubits=args.num_qubits)
        print("=== Basic Circuit ===")
        print(qc.draw(output='text'))

        counts = run_circuit_simulation(qc)
        print("\nMeasurement Counts:")
        print(counts)
        sys.exit(0)

    if args.vqe:
        energy = run_vqe_eigensolver()
        print(f"VQE Eigenvalue: {energy}")
        sys.exit(0)

    if args.parametric_ansatz:
        qc = build_parametric_ansatz(num_qubits=3, reps=2)
        print("Parametric ansatz circuit:\n", qc.draw(output='text'))
        sys.exit(0)

    if args.cobyla_opt:
        def example_builder(params):
            from qiskit import QuantumCircuit
            qc = QuantumCircuit(1)
            # Just a placeholder
            return qc
        result = run_cobyla_optimization(example_builder, maxiter=5)
        print("COBYLA final params:", result)
        sys.exit(0)

    if args.spsa_opt:
        def example_builder(params):
            from qiskit import QuantumCircuit
            qc = QuantumCircuit(1)
            return qc
        result = run_spsa_optimization(example_builder, maxiter=5)
        print("SPSA final params:", result)
        sys.exit(0)

    if args.visualize_states:
        demo_visualization()
        sys.exit(0)

    if args.circuit_debug:
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0,1)
        debug_result = debug_quantum_circuit(qc)
        print("Debug result:", debug_result)
        explanation = explain_debugging_issue(debug_result)
        print("Explanation:", explanation)
        sys.exit(0)

    if args.noise_test:
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(1,1)
        qc.h(0)
        qc.measure(0,0)
        counts = run_with_noise(qc)
        print("Counts with noise:", counts)
        print("Noise Impact Explanation:", explain_noise_impact())
        sys.exit(0)

    if args.compare_opts:
        def dummy_objective(x):
            return sum(val*val for val in x)
        init_point = [0.5, -0.3]
        results = compare_optimizers(dummy_objective, init_point, maxiter=5)
        for k, v in results.items():
            print(k, "=> params:", v[0], " cost:", v[1])
        sys.exit(0)

    if args.anneal_sim:
        final_state = simulated_quantum_annealing(num_steps=5)
        explanation = explain_annealing_results(final_state)
        print("Annealing final state:", final_state)
        print("Explanation:", explanation)
        sys.exit(0)

    if args.depth_opt:
        from qiskit import QuantumCircuit
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.h(0)
        qc.cx(0,1)
        optimized_qc = reduce_circuit_depth(qc)
        msg = analyze_depth_reduction(qc, optimized_qc)
        print("Depth optimization result:")
        print(optimized_qc.draw(output='text'))
        print("Analysis:", msg)
        sys.exit(0)

    print("No flag provided. Use --help for options.")

if __name__ == "__main__":
    main()

