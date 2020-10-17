from openfermion.ops import QubitOperator
from qiskit.aqua.operators.legacy.weighted_pauli_operator import WeightedPauliOperator
from qiskit.quantum_info import Pauli

def qubitop_to_pauliop(n_qubits, qubit_operator):
    """Convert an openfermion QubitOperator to a qiskit WeightedPauliOperator.
    Args:
        qubit_operator ("QubitOperator"): Openfermion QubitOperator to convert to a qiskit.WeightedPauliOperator.
    Returns:
        paulis ("WeightedPauliOperator"): Qiskit WeightedPauliOperator.
    """
    if not isinstance(qubit_operator, QubitOperator):
        raise TypeError("qubit_operator must be an openFermion QubitOperator object.")
    paulis = []

    for qubit_terms, coefficient in qubit_operator.terms.items():
        count=0
        pauli_label = ['I' for _ in range(n_qubits)]
        coeff = coefficient
        
        for tensor_term in qubit_terms:
            pauli_label[tensor_term[0]] = tensor_term[1]
                    
        paulis.append([coeff, Pauli.from_label(pauli_label)])
    
    pauliOp = WeightedPauliOperator(paulis)
    
    return pauliOp